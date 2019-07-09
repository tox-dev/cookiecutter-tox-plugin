import sys
from configparser import ConfigParser
from operator import attrgetter

import six
from pathlib2 import Path

ROOT = Path(__file__).absolute().parents[1]


def test_run_cookiecutter_and_plugin_tests(cookies, monkeypatch, call_subprocess):
    """Create a new plugin via cookiecutter and run its tests."""
    monkeypatch.chdir(ROOT)
    monkeypatch.setenv(str("GIT_COMMITTER_NAME"), str("committer joe"))
    monkeypatch.setenv(str("GIT_AUTHOR_NAME"), str("author joe"))
    monkeypatch.setenv(str("EMAIL"), str("joe@magic.com"))

    result = cookies.bake(
        extra_context={
            "full_name": "Happy Harry",
            "email": "harry@donotreply.com",
            "github_username": "happy_harry",
            "plugin_name": "foo-bar",
            "docs_tool": "sphinx",
            "license": "MIT",
        }
    )
    assert result.exit_code == 0, result.exception

    project = Path(str(result.project))
    assert project.name == "tox-foo-bar"
    assert project.is_dir()

    tree = make_dir_tree(project, filter_folder=lambda p: p.name == ".git")
    assert tree == {
        "tox-foo-bar": [
            ".git",
            ".gitignore",
            ".pre-commit-config.yaml",
            "LICENSE",
            "MANIFEST.in",
            "README.md",
            "azure-pipelines.yml",
            {"docs": ["conf.py", "index.rst"]},
            "pyproject.toml",
            "readthedocs.yml",
            "setup.cfg",
            "setup.py",
            {"src": [{"tox_foo_bar": ["__init__.py", "plugin.py"]}]},
            {
                "tests": [
                    "conftest.py",
                    {"integration": ["test_tox_tox_foo_bar_int.py"]},
                    {"unit": ["test_tox_tox_foo_bar.py", "test_version.py"]},
                ]
            },
            "tox.ini",
        ]
    }
    envs = current_envs(call_subprocess, project)
    cmd = [str(Path(sys.executable).parent / "tox"), "-vve", ",".join(envs)]
    monkeypatch.setenv(str("DIFF_AGAINST"), str("master"))
    call_subprocess(cmd, cwd=str(project))


def make_dir_tree(path, filter_folder=None):
    if path.is_file():
        return path.name
    elif path.is_dir():
        if filter_folder is not None and filter_folder(path):
            return path.name
        return {
            path.name: [
                make_dir_tree(i, filter_folder)
                for i in sorted(path.iterdir(), key=attrgetter("name"))
            ]
        }
    else:
        raise ValueError(path)


def current_envs(call_subprocess, project):
    cmd = [sys.executable, "-m", "tox", "--showconfig", "-a"]
    code, out, _ = call_subprocess(cmd, allow_fail=True, cwd=str(project))
    assert code == 0
    parser = ConfigParser()
    parser.read_string(six.text_type(out))
    envs = [
        n
        for n, e in (
            (env, parser[key]["basepython"])
            for env, key in ((s[8:], s) for s in parser.sections() if s.startswith("testenv:"))
        )
        if n != ".package"
        and (e == sys.executable or e == "python{}.{}".format(*sys.version_info[0:2]))
    ]
    if sys.version_info[0:2] < (3, 6):  # black requires python 3.6+
        envs.remove("fix_lint")
    if sys.version_info[0:2] < (3, 5):  # sphinx 2.0 requires python 3.5+
        envs.remove("docs")
        envs.remove("dev")
    return envs
