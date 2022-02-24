import json
from itertools import product
from random import choice
from os.path import join
from pathlib import Path

from mako.template import Template
from mako.lookup import TemplateLookup


STUDENTS = {
    "0": "Сухоплюев Илья",
    "1": "Антипин Дмитрий",
    "2": "Даровских Георгий",
    "3": "Имамутдинов Ильдар",
    "4": "Карманов Роман",
    "5": "Карташов Матвей",
    "6": "Кочнев Максим",
    "7": "Минибаев Роберт",
    "8": "Михайлов Данил",
    "9": "Мухаметянов Давлет",
    "10": "Некомкин Никита",
    "11": "Павлов Евгений",
    "12": "Рожков Илья",
    "13": "Самигуллин Амирхан",
    "14": "Скругин Даниил",
    "15": "Уасов Багжан",
    "16": "Файрузов Адель",
    "17": "Фархутдинов Радмир",
    "18": "Филиппов Дмитрий",
    "19": "Фомагин Олег",
    "20": "Хаертдинов Адель",
    "21": "Хомутов Даниил",
    "22": "Шарафутдинов Нияз",
    "23": "Шикалов Владислав",
    "24": "Крупоткин Сигурд",
}

COLORS = [
    "AliceBlue",
    "Chocolate",
    "Chartreuse",
    "Crimson",
    "DarkBlue",

    "DarkGoldenRod",
    "DarkMagenta",
    "DarkOrange",
    "DarkRed",
    "DeepPink",

    "DarkViolet",
    "DodgerBlue",
    "ForestGreen",
    "Gold",
    "GreenYellow",

    "IndianRed ",
    "LightPink",
    "Lime",
    "Maroon",
    "MidnightBlue",

    "Navy",
    "Olive",
    "Peru",
    "Plum",
    "Salmon",
]

# 2 модуль Февраля - Тетрис

DIRECTIONS = {
    "BOTTOM",
    "RIGHT",
    "UP",
    "LEFT",
}

DIRECTION_LABELS = {
    "BOTTOM": "Сверху-Вниз",
    "RIGHT": "Слева-Вправо",
    "UP": "Снизу-Вверх",
    "LEFT": "Справа-Налево",
}

NEW_FIGURE_SIDE_LABEL = {
    "BOTTOM": "Вверху",
    "RIGHT": "Слева",
    "UP": "Внизу",
    "LEFT": "Справа",
}

ARROW_LABELS = {
    "BOTTOM": {
        "MOVE-ARROWS": "Стрелки Влево-Вправо",
        "SPEEDUP-ARROW": "Вниз",
        "TRANSPOND-ARROW": "Вверх",
    },
    "RIGHT": {
        "MOVE-ARROWS": "Стрелки Вверх-Вниз",
        "SPEEDUP-ARROW": "Вправо",
        "TRANSPOND-ARROW": "Влево",
    },
    "UP": {
        "MOVE-ARROWS": "Стрелки Влево-Вправо",
        "SPEEDUP-ARROW": "Вверх",
        "TRANSPOND-ARROW": "Вниз",
    },
    "LEFT": {
        "MOVE-ARROWS": "Стрелки Вверх-Вниз",
        "SPEEDUP-ARROW": "Влево",
        "TRANSPOND-ARROW": "Вправо",
    },
}

NUMBERS_OF_KNOWN_FIGURES = list({1, 2, 3, })

FIGURES = {
    (
        (1, ),
        (1, ),
        (1, ),
        (1, ),
    ),
    (
        (1, 1),
        (1, 1),
    ),
    (
        (1, 0),
        (1, 0),
        (1, 1),
    ),
    (
        (0, 1),
        (0, 1),
        (1, 1),
    ),
    (
        (1, 0),
        (1, 1),
        (1, 0),
    ),
    (
        (1, 0),
        (1, 1),
        (0, 1),
    ),
    (
        (0, 1),
        (1, 1),
        (1, 0),
    ),
}

FIGURES_SETS = [ FIGURES - {figure,} for figure in FIGURES ]

SPEED = list({1, 1.5, 2, 2.5, 3})

def generate_module_2_options():
    for (std_num, (direction, figures_set)) in enumerate(list(product(DIRECTIONS, FIGURES_SETS))):
        yield {
            'direction': direction,
            'figures_set': list(figures_set),
            'numbers_of_known_figures': choice(NUMBERS_OF_KNOWN_FIGURES),
            'speed': choice(SPEED),
            "direction_label": DIRECTION_LABELS[direction],
            "arrow_labels": ARROW_LABELS[direction],
            "new_figure_side_label":NEW_FIGURE_SIDE_LABEL[direction],
            "std_num": std_num,
            "student_name": STUDENTS.get(str(std_num), f"std{std_num}"),
            "color": choice(COLORS),
        }


def generate_module_2_task(option:dict, output_dir:str, std_num:int):
    lookup = TemplateLookup(directories=["."])

    std_output_dir = join(output_dir, f"std{std_num}")
    Path(std_output_dir).mkdir(exist_ok=True, parents=True)

    with open(join(std_output_dir, "task.md"), "w", encoding="utf8") as f:
        template = lookup.get_template('feb_module2.md')
        f.write(template.render(**option))

    for file_suffix in ["index.html", "game.html", "results.html"]:
        with open(join(std_output_dir, file_suffix), "w", encoding="utf8") as f:
            template = lookup.get_template(f'feb_{file_suffix}')
            f.write(template.render(**option))

    with open(join(std_output_dir, "figures.json"), "w", encoding="utf8") as f:
        json.dump(list(option["figures_set"]),
                  f,
                  indent=4)

    with open(join(std_output_dir, "options.json"), "w", encoding="utf8") as f:
        json.dump(dict(**option),
                  f,
                  indent=4)



if __name__ == "__main__":
    output_dir = join("feb", "moudle2")
    for (i, option) in enumerate(generate_module_2_options()):
        generate_module_2_task(option, output_dir, i)
