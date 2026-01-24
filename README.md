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
