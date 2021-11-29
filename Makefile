.RECIPEPREFIX = >

# Remove build artefacts
.PHONY: clean
clean:
> @echo Cleaning
> @rm -rf build

# Rebuild the pickled `.dat` file from `rmsfact.txt`
.PHONY: build_binary_data
build_binary_data:
> @echo Building binary data
> @rm -f rmsfact/data/rmsfact.dat
> @python rmsfact/data/build_rmsfact.py

# Build the package in wheel and source form
.PHONY: build
build: clean build_binary_data
> @echo Building package
> @python -m build

# Build the package and install locally for development
.PHONY: install_dev
install_dev: build
> @echo Installing locally
> @python -m pip install -e .

# Install
.PHONY: install
install: build
> @echo Installing
> @python -m pip install .

# Build the package and upload to TestPyPI
.PHONY: upload_test
upload_test: test build
> @echo Uploading to testpypi
> @python -m twine upload --repository testpypi dist/*

# Build the package and upload to PyPI
.PHONY: upload
upload: test build
> @echo Uploading to PyPi
> @python -m twine upload dist/*

# Run unit tests
.PHONY: test
test: clean build_binary_data
> @echo Running tests
> @python test
