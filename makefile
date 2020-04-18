install:
	pip install setuptools wheel twine bumpversion

activate:
	source ../venv38/bin/activate

clear:
	rm -rf build dist *.egg-info

build: clear
	python setup.py sdist bdist_wheel
	# python setup.py bdist_wheel

check:
	twine check dist/*

test:
	pip3 install --upgrade --no-deps --force-reinstall craftsmen
	# twine upload --repository-url https://test.pypi.org/legacy/ dist/*
	# pip install --index-url https://test.pypi.org/simple/ craftsmen

upload:
	twine upload dist/*
