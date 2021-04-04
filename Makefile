.PHONY: build
build:
	rm -rf dist/*
	python setup.py sdist bdist_wheel

.PHONY: publish
publish: build
	twine upload dist/*
