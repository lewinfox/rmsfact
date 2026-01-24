.RECIPEPREFIX = >

# Lint, format, test
.PHONY: all
all: clean check format test

# Remove build artefacts
.PHONY: clean
clean:
> @echo Cleaning
> @rm -rf build dist

# Build the package in wheel and source form
.PHONY: build
build: clean
> @echo Building package
> @uv build

# Install dependencies and set up development environment
.PHONY: install_dev
install_dev:
> @echo Setting up development environment
> @uv sync

# Install the package
.PHONY: install
install: build
> @echo Installing package
> @uv pip install dist/*.whl

# Build the package and upload to TestPyPI
.PHONY: upload_test
upload_test: test build
> @echo Uploading to testpypi
> @uv run twine upload --repository testpypi dist/*

# Build the package and upload to PyPI
.PHONY: upload
upload: test build
> @echo Uploading to PyPi
> @uv run twine upload dist/*

# Run unit tests
.PHONY: test
test: clean
> @echo Running tests
> @uv run pytest

# Format code
.PHONY: format
format:
> @uv run ruff check --select I --fix
> @uv run ruff format

# Lint
.PHONY: check
check:
> @uv run ruff check
