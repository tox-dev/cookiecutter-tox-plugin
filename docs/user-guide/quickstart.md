# User Guide

## What is Cookiecutter?

[Cookiecutter] is a command-line utility that creates projects from **cookiecutters** (project
templates), e.g. creating a Python package project from a Python package project template.

## Installation

Cookiecutter is available on [PyPI]. Use ``pip`` to download and install:

```no-highlight
$ pip install cookiecutter
```

## Usage

You can generate a new project from a template by using the following command:

```no-highlight
$ cookiecutter https://github.com/tox-dev/cookiecutter-tox-plugin
```

This will not only ``git clone`` the template but also start the generation process.

## Template Variables

Each Cookiecutter template uses variables, which are specified in the template, that
it replaces in all of the directory and file names, but also in text such as source code
or markdown formats.

### Plugin Details

Cookiecutter prompts you for information regarding your plugin based on aforementioned variables:

```no-highlight
full_name [Oliver Bestwalter]: Somebody Else
email [oliver@bestwalter.de]: somebody@elsewhere.com
github_username [obestwalter]: somebody_else
plugin_name [foobar]: awesome
pkg_name [tox_foobar]:
module_name [plugin]:
entry_point [tox_foobar.plugin]:
short_description [A simple plugin to use with tox]:
version [0.1.0]:
tox_version [3.0.0]:
Select docs_tool:
1 - mkdocs
2 - sphinx
3 - none
Choose from 1, 2, 3 [1]:
Select license:
1 - MIT
2 - BSD-3
3 - GNU GPL v3.0
4 - Apache Software License 2.0
5 - Mozilla Public License 2.0
Choose from 1, 2, 3, 4, 5 [1]:

INFO:post_gen_project:Initializing docs for mkdocs
INFO:post_gen_project:Moving doc_sources/mkdocs/index.md to docs/index.md.
INFO:post_gen_project:Moving doc_sources/mkdocs/mkdocs.yml to /home/ob/do/tox-dev/tox-foobar/mkdocs.yml.
INFO:post_gen_project:Remove temporary folder: doc_sources
INFO:post_gen_project:Remove temporary folder: licenses
INFO:post_gen_project:Remove temporary folder: macros
```

The values in the square brackets (f.i. ``[foobar]``) are defaults for the according variables.

## Project Generation

Once you answered the questions, Cookiecutter renders the the project:

```no-highlight
tox-awesome/
├── tox.ini
├── .travis.yml
├── appveyor.yml
├── mkdocs.yml
├── LICENSE
├── MANIFEST.in
├── README.rst
├── docs
│   └── index.md
├── setup.py
├── tests
│   ├── conftest.py
│   └── test_tox_awesome.py
└── tox_awesome
    ├── __init__.py
    └── plugin.py
```

There you go - you just created a minimal tox plugin:

  [Cookiecutter]: https://github.com/audreyr/cookiecutter
  [PyPI]: https://pypi.org/project/cookiecutter/1.0.0
