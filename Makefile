.PHONY: build
build:
	rm -rf dist/*
	python -m build

.PHONY: publish
publish: build
	twine upload dist/*

.PHONY: publish-test
publish-test: build
	twine upload --repository testpypi dist/*
