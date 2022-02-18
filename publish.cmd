git checkout gh-pages
git merge main
python publish-zettelkasten.py
git add -f docs/
git ci -m "publish"
git push -f
git checkout main
