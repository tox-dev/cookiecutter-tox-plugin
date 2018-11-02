[![Travis CI Build Status][travis_badge]][travis] [![Documentation Status][docs_badge]][documentation]

# Cookiecutter tox plugin

Minimal [Cookiecutter] template for authoring [tox] plugins to change or extend the behaviour of tox.

## Getting Started

Install [Cookiecutter] and generate a new tox plugin project:

```no-highlight
$ pip install -U cookiecutter
$ cookiecutter https://github.com/tox-dev/cookiecutter-tox-plugin
```

Cookiecutter prompts you for information regarding your plugin:

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

There you go - you just created a minimal tox plugin:

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

## Features

- Installable [PyPI] package featuring a `setup.py`.
- Test suite running [tox] and [pytest] that makes sure your plugin is working as expected
- Comprehensive `README.rst` file that contains useful information about your
  plugin
- Continuous integration configuration for [Travis CI] and [AppVeyor]
- Optional documentation with either [Sphinx] or [MkDocs]
- Choose from several licenses, such as [MIT], [BSD-3], [Apache v2.0], [GNU GPL v3.0], or [MPL v2.0]

## Requirements to Submit a Plugin

If you plan on submitting your plugin to the [tox-dev organization] you need
to meet the following requirements:

-   PyPI presence with a setup.py that contains a license, tox-
    prefixed, version number, authors, short and long description.
-   a tox.ini for running tests using tox.
-   a README describing how to use the plugin and on which platforms
    it runs.
-   a LICENSE file or equivalent containing the licensing information,
    with matching info in setup.py.
-   an issue tracker.

Please see the official guidelines at [Submit a Plugin].

## Resources

Please consult the [tox] docs for more information on hooks at
[tox plugin/hooks reference].

## Contribute

We welcome you to contribute to this project. Please visit the
[documentation] to get started!

## Issues

If you encounter any problems, please [file an issue] along with a
detailed description.

## Code of Conduct

Everyone interacting in the cookiecutter tox plugin project's codebases,
issue trackers, chat rooms, and mailing lists is expected to follow the [PyPA
Code of Conduct].

## License

Distributed under the terms of the [MIT license], cookiecutter tox
plugin is free and open source software

[![OSI certified][osi_certified]][OSI]


  [tox-dev organization]: https://github.com/tox-dev/
  [travis_badge]: https://travis-ci.org/tox-dev/cookiecutter-tox-plugin.svg?branch=master
  [travis]: https://travis-ci.org/tox-dev/cookiecutter-tox-plugin (See Build Status on Travis CI)
  [docs_badge]: https://readthedocs.org/projects/cookiecutter-tox-plugin/badge/?version=latest
  [documentation]: https://cookiecutter-tox-plugin.readthedocs.io/en/latest/ (Documentation)
  [Cookiecutter]: https://github.com/audreyr/cookiecutter
  [pytest]: https://docs.pytest.org
  [PyPI]: https://pypi.org
  [tox]: https://tox.readthedocs.io/en/latest/
  [Submit a Plugin]: https://github.com/tox-dev/tox/blob/master/CONTRIBUTING.rst#submitting-plugins-to-tox-dev
  [tox plugin/hooks reference]: http://tox.readthedocs.io/en/latest/plugins.html
  [MIT license]: http://opensource.org/licenses/MIT
  [file an issue]: https://github.com/tox-dev/cookiecutter-tox-plugin/issues
  [Sphinx]: http://sphinx-doc.org/
  [MkDocs]: http://www.mkdocs.org/
  [MIT]: http://opensource.org/licenses/MIT
  [MPL v2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
  [BSD-3]: http://opensource.org/licenses/BSD-3-Clause
  [GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
  [Apache v2.0]: http://www.apache.org/licenses/LICENSE-2.0
  [Travis CI]: https://travis-ci.com/
  [AppVeyor]: http://www.appveyor.com/
  [PyPA Code of Conduct]: https://www.pypa.io/en/latest/code-of-conduct/
  [Shortbread]: https://github.com/audreyr/cookiecutter/releases/tag/1.4.0
  [osi_certified]: https://opensource.org/trademarks/osi-certified/web/osi-certified-120x100.png
  [OSI]: https://opensource.org/
