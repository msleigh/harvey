Harvey
======

Harvey is a simple 1D diffusion solver with a range of built-in test cases based on
analytic solutions. It's a mixed Python/Fortran code, with a top-level control layer
written in Python calling a Fortran kernel.

<img src="https://img.shields.io/github/v/release/msleigh/harvey?include_prereleases"> <img src="https://img.shields.io/github/license/msleigh/harvey"> <img src="https://img.shields.io/tokei/lines/github/msleigh/harvey"> <img src="https://img.shields.io/github/last-commit/msleigh/harvey">

<img src="https://img.shields.io/badge/code%20style-black-lightgrey">

![Build status (`main`)](https://github.com/msleigh/harvey/actions/workflows/build.yml/badge.svg?branch=main)

It can be executed by running the the top-level `harvey.py` directly, but in most cases
a problem-specific top-level Python script should be written that calls the code as a
solver. The included test cases demonstrate how to do this. The test suite is
controlled by [Robot Framework](http://robotframework.org).

## Dependencies

### Build

- Python 3
- Numpy (to provide f2py)
- Fortran compiler (tested with gfortran)

### Built-in tests

- Robot Framework (runs QA tests and presents results)
- Docutils (needed for Robot Framework to read ReStructuredText files)
- Matplotlib (creates plots of test results)

### Documentation

There are two options for the documentation dependencies:

- Docker (recommended): Docker Engine only.
- Local install: Doxygen, Graphviz, Doxypypy (Python package), and LaTeX (for PDF
  output).

## Installation

Use `uv` to install the necessary dependencies:

    uv venv
    source .venv/bin/activate
    uv sync

(This excludes the documentation dependencies.)

Install `gfortran` for the Fortran build:

    # macOS (Homebrew)
    brew install gcc

    # Linux (Debian/Ubuntu)
    sudo apt-get install gfortran

    # Linux (Fedora/RHEL)
    sudo dnf install gcc-gfortran

## Usage

### Building

To compile the Fortran into a shared object library:

    make harvey

This runs:

    f2py -c --f90flags="-ffree-form" -m harfort <src>

where `<src>` is a list of the Fortran source-code files. The result is a `.so` shared
object which can be called from the top-level Python code.

It assumes the `f2py` command-line utility is available; this is installed as part of
the `numpy` package.

### Cleaning

To clean up intermediate build files etc.:

    make clean

and to clean executables to force a fresh full new build:

    make cleaner

(This also removes the documentation.)

### Building the documentation

You can build the docs either by installing the dependencies locally or by using the
provided Docker container. The default `make doc` target uses Docker.

#### Option 1: Docker (recommended)

    make doc

#### Option 2: Local install

Install the documentation dependencies on your machine (Doxygen, Graphviz, LaTeX,
and the `doxypypy` Python package). For example:

    # macOS (Homebrew)
    brew install doxygen graphviz mactex
    python3 -m pip install doxypypy

    # Linux (Debian/Ubuntu)
    sudo apt-get install doxygen graphviz texlive-latex-base texlive-latex-extra texlive-fonts-recommended
    python3 -m pip install doxypypy

Build the docs locally (from the repository root):

    make doxygen.log

If you run Doxygen directly instead of `make`, invoke it from the repository
root so the paths in `doc/Doxyfile` resolve correctly:

    doxygen doc/Doxyfile

#### Opening the output

The output is created in `build/Doc`. Open locally with:

    open build/Doc/html/index.html

(or use `xdg-open` for Linux).

LaTeX documentation is also built (in `build/Doc/latex`). Run:

    make -C build/Doc/latex pdf

to compile the PDF output.

### Running

#### Sanity-check run

To run the code 'as-is', after building (above), execute:

    export PYTHONPATH="${PWD}/build:${PYTHONPATH:-}"
    src/harvey.py

A built-in problem defined in `src/harvin.py` is executed as the most basic check that
the build has completed successfully. Output data is written to the file `harvey.out`.
A reference copy of the expected output is stored in `src/harvey.kgo`:

    diff src/harvey.kgo harvey.out

#### Running the test suite

To run the full test suite:

    make test

After setting up, this executes Robot Framework against the test suite defined in
`qa/hvy_qa_test.rst`. For each test `<i>`, the file `test<i>.py` controls the overall
QA test, including the generation of the analytic solution results, and the final
checks and comparisons. The file `test<i>_in.py` is the problem-dependent input file
for the run of `harvey`.

Output is created in `build/QA`. For each problem a `test<i>.out` file contains the
results and a PNG file shows a plot of the numerical vs. analytic solution(s). The
overall test report created by Robot Framework is in `build/QA/report.html`. In
the event of test failures, `build/QA/log.html` created by Robot Framework contains
more detailed information. Fortran stdout/stderr from each run is captured in
`test<i>.log` so the terminal output stays focused on PASS/FAIL results.

#### Specifying a new problem

To create a new run, create an input definition file (a Python script, with a
`.py` extension), containing a `define()` function that sets up the problem
specification. The example input file `src/harvey.in` provides a template, and the
built-in test problem suite (described below) provides other examples. Run with a
user-defined input file:

    src/harvey.py -i <test_file>

where the string `<test_file>` should _omit_ the `.py` extension.
