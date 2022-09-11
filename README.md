# NEO Linear Algebra

**Author:** Sajid Al Sanai

**License:** MIT License

## 1. Motivation

**NEO Linear Algebra** is a lightweight Python package designed for Matrix operations in Linear Algebra.

[...]

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

## 3. Files

The directory structure for this repository is detailed below:

```bash
.
├── neolinearalgebra
│   ├── Matrix.py
│   └── __init__.py
├── .gitignore
├── LICENSE.txt
├── README.md
├── setup.cfg
├── setup.py
└── test.py
```

Setup and configuration files for package installation is in the root **.** directory. The contents of the package is stored in **./neolinearalgebra/**. The singular class is *Matrix*.

## 4. Unit Testing

The aforementioned file *test.py* for performing unit testing is included in the main directory of the repository. You may append the program with additional functions for unit testing *Matrix.py*.

Please perform unit testing after you have upgraded your version of the package locally during open source development.

To perform unit testing, use the following bash code in a UNIX-based environment:

```bash
cd ./neolinearalgebra/
python3 -m pip install --upgrade .
python3 -v test.py
```

*or*

```bash
cd ./neolinearalgebra/
python3 -m pip install --upgrade .
chmod +x test.py
./test.py -v
```

## 5. Usage

[...]

## 6. Documentation

Docstrings highlight the behaviour of class attributes and class methods within files in this repository. For more detailed information, you may consult my [blog post](https://sajidsarker.github.io/) for a reproduction of documentation on package functionality.

[...]
