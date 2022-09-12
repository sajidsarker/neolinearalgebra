# NEO Linear Algebra

**Author:** Sajid Al Sanai

**License:** MIT License

**Version:** 0.1.5

**Article:** [NEO Linear Algebra for Python](https://sajidsarker.github.io/2022/09/10/neo-linear-algebra-for-python.html)

## Table of Contents
1. [Motivation](https://github.com/sajidsarker/neolinearalgebra#1-motivation)
2. [Installation](https://github.com/sajidsarker/neolinearalgebra#2-installation)
3. [Build](https://github.com/sajidsarker/neolinearalgebra#3-build)
4. [Files](https://github.com/sajidsarker/neolinearalgebra#4-files)
5. [Unit Testing](https://github.com/sajidsarker/neolinearalgebra#5-unit-testing)
6. [Usage](https://github.com/sajidsarker/neolinearalgebra#6-usage)
7. [Documentation](https://github.com/sajidsarker/neolinearalgebra#7-documentation)

## 1. Motivation

**NEO Linear Algebra** is a lightweight Python package designed for Matrix operations in Linear Algebra.

I was inspired to program this from scratch as part of a light review of the absolute fundamentals of Linear Algebra and my own first attempt at the development of a Python package for open source. I was also inspired by rewatching The Matrix quadrilogy.

## 2. Installation

This project consists of a directory for a singular *Matrix* class file.

You may install this package locally on your machine or download through the Python pip package manager.

To download this repository and **install** the package locally on your machine, use the following bash code in a UNIX-based environment:

```bash
git clone https://github.com/sajidsarker/neolinearalgebra.git
cd ./neolinearalgebra/
python3 -m pip install --upgrade pip
python3 -m pip install .
```

To download this repository and **upgrade** the package locally on your machine, use the following bash code in a UNIX-based environment:
```bash
git clone https://github.com/sajidsarker/neolinearalgebra.git
cd ./neolinearalgebra/
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade .
```

To **uninstall** the package locally on your machine, navigate to the repository directory in your terminal use the following bash code in a UNIX-based environment:
```bash
python3 -m pip uninstall .
cd ../ && rm -rf ./neolinearalgebra
```

To **install** this package through the Python pip package manager, use the following bash code in a UNIX-based environment:

```bash
python3 -m pip install --upgrade pip
python3 -m pip install neolinearalgebra
```

To **upgrade** this package through the Python pip package manager, use the following bash code in a UNIX-based environment:

```bash
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade neolinearalgebra
```

To **uninstall** this package through the Python pip package manager, use the following bash code in a UNIX-based environment:

```bash
python3 -m pip uninstall neolinearalgebra
```

## 3. Build

To download this repository and **build** the package locally on your machine, use the following bash code in a UNIX-based environment:
```bash
git clone https://github.com/sajidsarker/neolinearalgebra.git
cd ./neolinearalgebra/
python3 -m pip build . --wheel
```

## 4. Files

The directory structure for this repository is detailed below:

```bash
/
├── Documentation/
│   └── Documentation.html
├── src/
│   └── neolinearalgebra/
│       ├── Matrix.py
│       └── __init__.py
├── tests/
│   └── test.py
├── .gitignore
├── LICENSE.txt
├── README.md
├── pyproject.toml
├── setup.cfg
└── setup.py
```

Setup and configuration files for package installation is in the root **.** directory. The contents of the package is stored in **./neolinearalgebra/**. The singular class is *Matrix*.

## 5. Unit Testing

The aforementioned file *test.py* for performing unit testing is included in the main directory of the repository. You may append the program with additional functions for unit testing *Matrix.py*.

Please only perform unit testing after you have upgraded your version of the package locally during open source development.

To perform unit testing, use the following bash code in a UNIX-based environment:

```bash
cd ./neolinearalgebra/tests/
python3 -v test.py
```

*or*

```bash
cd ./neolinearalgebra/tests/
chmod +x test.py
./test.py -v
```

## 6. Usage

To import **NEO Linear Algebra** into your Python project, use the following *import* declaration at the start of your program code:

```python
from neolinearalgebra import Matrix
```

## 7. Documentation

Docstrings highlight the behaviour of class attributes and class methods within files in this repository. A comprehensive reference on class attributes and methods are present in the **./Documentation** folder.

For information on the motivation behind this project, you may consult my [blog post](https://sajidsarker.github.io/2022/09/10/neo-linear-algebra-for-python.html) for an overview.
