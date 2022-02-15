import argparse
import os
import shutil
from os.path import join
from pathlib import Path

from markdown import markdown

from mako.template import Template
from mako.lookup import TemplateLookup


def transform_note(filepath: str, templates_dir: str) -> str:
    with open(filepath, "r", encoding="utf8") as f:
        md_text = f.read()

    lookup = TemplateLookup(directories=[templates_dir])
    template = lookup.get_template('index.html')
    return template.render(content=markdown(md_text))


def walk_on_zettelkasten(args):
    os.makedirs(args.output_dir, exist_ok=True)
    for root, _, files in os.walk(args.input_dir):
        for filename in files:
            filename = Path(filename)
            if filename.suffix != ".md":
                shutil.copy(
                    join(root, filename),
                    join(args.output_dir, filename)
                )
                continue

            filepath = join(root, filename)
            html = transform_note(filepath, args.templates_dir)

            if "index" in filename.name:
                filename = filename.with_name('index')

            output_filepath = join(args.output_dir,
                                   filename.with_suffix(".html"))
            with open(output_filepath, "w", encoding="utf8") as f:
                f.write(html)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-dir', default="zettelkasten", type=str)
    parser.add_argument('-o', '--output-dir', default="docs", type=str)
    parser.add_argument('-t', '--templates-dir', default="templates", type=str)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    walk_on_zettelkasten(args)
