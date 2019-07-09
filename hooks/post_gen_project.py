import distutils.spawn
import logging
import os
import shutil
import subprocess

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("post_gen_project")

DOC_SOURCES = "doc_sources"
ALL_TEMP_FOLDERS = DOC_SOURCES, "licenses"
DOC_TYPE_FILES_MAP = {"mkdocs": ["index.md", "mkdocs.yml"], "sphinx": ["conf.py", "index.rst"]}


def move_doc_files(which, map_=None, doc_sources=DOC_SOURCES):
    if map_ is None:
        map_ = DOC_TYPE_FILES_MAP
    if which == "none":
        return
    root = os.getcwd()
    docs = "docs"
    log.info("Initializing docs for %s" % which)
    if not os.path.exists(docs):
        os.mkdir(docs)
    for item in map_[which]:
        dst, name = (root, item[1:]) if item.startswith("/") else (docs, item)
        src_path = os.path.join(doc_sources, which, name)
        dst_path = os.path.join(dst, name)
        log.info("Moving {} to {}.".format(src_path, dst_path))
        if os.path.exists(dst_path):
            os.unlink(dst_path)
        os.rename(src_path, dst_path)


def tidy_up(temp_folders=ALL_TEMP_FOLDERS):
    for folder in temp_folders:
        log.info("Remove temporary folder: {}".format(folder))
        shutil.rmtree(folder)


def git_init():
    git = distutils.spawn.find_executable("git")
    subprocess.check_call([str(git), "init"])
    subprocess.check_call([str(git), "add", "--all"])
    subprocess.check_call(
        [str(git), "commit", "-m", "initialize tox-{{cookiecutter.plugin_name}}"]
    )
    subprocess.check_call(
        [
            "git",
            "remote",
            "add",
            "origin",
            "https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.plugin_name}}.git",
        ]
    )


if __name__ == "__main__":
    move_doc_files("{{cookiecutter.docs_tool}}")
    tidy_up()
    git_init()
