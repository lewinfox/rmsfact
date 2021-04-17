.RECIPEPREFIX = >

.PHONY: build
build:
> rm -rf dist
> python -m build

.PHONY: upload_test
upload_test: build
> python -m twine upload --repository testpypi dist/*

.PHONY: upload
upload: build
> python -m twine upload dist/*
