setup:
	python setup.py bdist_wheel

check:
	twine check dist/*

upload:
	twine upload --skip-existing dist/*
