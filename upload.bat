pip install twine 
python3 setup.py sdist
del dist
mkdir dist
python3 -m twine upload dist/*
del dist
pause