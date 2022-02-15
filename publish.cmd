git checkout gh-pages
git rebase main
. venv\Scripts\activate
python publish-zettelkasten.py
git add -f docs/
git ci -m "publish"
git push -f
git checkout main
