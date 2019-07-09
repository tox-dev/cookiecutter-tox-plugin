def test_version():
    pkg = __import__("{{cookiecutter.pkg_name}}", fromlist=["__version__"])
    assert pkg.__version__
