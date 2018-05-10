cd output
git add .
git commit -m "Updated site"
git push -u origin master
cd ..
echo '*.pyc' >> .gitignore #don't need pyc files
git add .
git commit -m "Updated site"
git push -u origin master

