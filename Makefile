.RECIPEPREFIX = >

# Rebuild the pickled `.dat` file from `rmsfact.txt`
.PHONY: build_binary_data
build_binary_data:
> rm -f rmsfact/data/rmsfact.dat
> python rmsfact/data/build_rmsfact.py

# Build the package in wheel and source form
.PHONY: build
build: build_binary_data
> rm -rf dist
> python -m build

# Build the package and install locally for development
.PHONY: install_dev
install_dev: build
> python -m pip install -e .

# Install
.PHONY: install
install: build
> python -m pip install .

# Build the package and upload to TestPyPI
.PHONY: upload_test
upload_test: build
> python -m twine upload --repository testpypi dist/*

# Build the package and upload to PyPI
.PHONY: upload
upload: build
> python -m twine upload dist/*
