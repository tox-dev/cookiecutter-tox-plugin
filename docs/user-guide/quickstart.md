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
full_name: Somebody Else
email: somebody@elsewhere.com
github_username: somebody_else
plugin_name: awesome
pkg_name [tox_awesome]:
module_name [plugin]:
entry_point [tox_awesome.plugin]:
short_description [A simple plugin to use with tox]:
tox_version [3.12.2]:
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
INFO:post_gen_project:Moving doc_sources/mkdocs/mkdocs.yml to mkdocs.yml.
INFO:post_gen_project:Remove temporary folder: doc_sources
INFO:post_gen_project:Remove temporary folder: licenses
Initialized empty Git repository in /home/ob/do/tox-dev/tox-awesome/.git/
[master (root-commit) abc1d23] initialize tox-awesome
```

The values in the square brackets (f.i. ``[foobar]``) are defaults for the according variables.

## Project Generation

Once you answered the questions, Cookiecutter renders the the project:

```no-highlight
tox-awesome/
├── azure-pipelines.yml
├── docs
│   └── index.md
├── .git
├── .gitignore
├── LICENSE
├── MANIFEST.in
├── .pre-commit-config.yaml
├── pyproject.toml
├── README.md
├── readthedocs.yml
├── setup.cfg
├── setup.py
├── src
│   └── tox_awesome
│       ├── __init__.py
│       └── plugin.py
├── tests
│   ├── conftest.py
│   ├── integration
│   │   └── test_tox_tox_awesome_int.py
│   └── unit
│       ├── test_tox_tox_awesome.py
│       └── test_version.py
└── tox.ini
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
