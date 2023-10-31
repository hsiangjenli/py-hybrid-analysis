clean:
	rm -rf build dist *.egg-info

pypi:
	python setup.py sdist --formats=zip
	twine check dist/*

html:
	pip install .
	cd docs && make html