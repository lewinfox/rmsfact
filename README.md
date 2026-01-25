# rmsfact

A port of the R package [`rmsfact`](https://cran.r-project.org/package=rmsfact) by Dirk Edelbuettel.

Display a randomly selected quote about Richard M. Stallman based on the collection in the 'GNU
Octave' function 'fact()' which was aggregated by Jordi Gutiérrez Hermoso based on the (now defunct)
site stallmanfacts.com (which is accessible only via <http://archive.org>).


# Installation

```bash
uv pip install rmsfact
```

Or with pip:

```bash
pip install rmsfact
```


# Usage

The package exports a single function `rmsfact()` which returns a single randomly-chosen "fact" as
a `str`.

```python
import rmsfact

rmsfact.rmsfact()
```

You can also run `python -m rmsfact` from a shell.


# Building from source

This project uses [uv](https://github.com/astral-sh/uv) for dependency management and building.

Clone the repository:

```bash
git clone https://github.com/lewinfox/rmsfact.git
cd rmsfact
```

Install uv if you don't have it:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Set up the development environment:

```bash
make install_dev
```

This will create a virtual environment, install dependencies, and set up the package for development.


# Making changes

To add a new fact you can edit `rmsfact/data/rmsfact.txt`. The text file is read directly when the package is imported, so no build step is needed.

```bash
echo "A new fact" >> rmsfact/data/rmsfact.txt
```

The `Makefile` provides several useful targets:

* `make install_dev`: Set up development environment with uv
* `make test`: Run unit tests with pytest
* `make build`: Build the package (creates source and wheel distributions)
* `make clean`: Remove build artifacts
* `make format`: Format code with ruff
* `make check`: Run linter checks

You can build the package with:

```bash
make build
```


# Releasing to PyPI

This project uses GitHub Actions to automatically publish to PyPI when you create a new GitHub release.

## First-time setup

You need to configure PyPI's Trusted Publishers feature (one-time setup):

1. Go to [PyPI](https://pypi.org/) and log in to your account
2. Navigate to your project's settings (or create the project first if it doesn't exist)
3. Go to the "Publishing" section
4. Add a new publisher with these settings:
   - **PyPI Project Name**: `rmsfact`
   - **Owner**: `lewinfox` (your GitHub username)
   - **Repository name**: `rmsfact`
   - **Workflow name**: `publish.yml`
   - **Environment name**: (leave blank)

## Creating a release

Once trusted publishing is configured, simply create a new GitHub release:

1. Update the version in [pyproject.toml](pyproject.toml:7)
2. Commit and push your changes
3. Create a new release on GitHub with a tag matching the version (e.g., `v0.5.0`)
4. The GitHub Action will automatically build and publish to PyPI

You can also manually publish with:

```bash
make upload
```
