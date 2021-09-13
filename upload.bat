pip install twine 
python3 setup.py sdist
mkdir dist
python3 -m twine upload dist/*
pause