# Publish a Plugin

There are several ways to publish a [tox] plugin.

Essentially tox plugins are not different from any other Python Package, so
you may want to create a distribution and submit it to the Python Package Index ([PyPI]).

By doing so, it enables your users to easily install them via ``pip``.

## Python Package Index

Submitting to [PyPI] that includes the following steps:

- Configuring your plugin (which is already covered in this template)
- Creating a distribution for your project
- Uploading your tox plugin to PyPI

Please see the official [Python Packaging User Guide] for detailed information.

## tox-dev Github Organization

If you plan on submitting your plugin to the [tox-dev organization] you need
to meet the following requirements:

-   PyPI presence with a setup.py that contains a license, tox-
    prefixed, version number, authors, short and long description.
-   a tox.ini for running tests using tox.
-   a README describing how to use the plugin and on which platforms
    it runs.
-   a LICENSE file or equivalent containing the licensing information,
    with matching info in setup.py.
-   an issue tracker unless you rather want to use the core Pytest
    issue tracker.

Please see the official guidelines at [Submit a Plugin].

  [tox-dev organization]: https://github.com/tox-dev/
  [Submit a Plugin]: https://github.com/tox-dev/tox/blob/master/CONTRIBUTING.rst#submitting-plugins-to-tox-dev
  [tox]: https://github.com/tox-dev/tox
  [PyPI]: https://pypi.org
  [Python Packaging User Guide]: https://python-packaging-user-guide.readthedocs.io/en/latest/distributing.html
