#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import re
import sys

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('pre_gen_project')


def validate_plugin_name(name):
    matcher = re.compile(r'^(?!tox)[-_a-zA-Z][-_a-zA-Z0-9]+$')
    if not re.match(matcher, name):
        log.error('Invalid value for plugin_name "%s"', name)
        log.info('Must match %s', matcher.pattern)
        log.info('Do not prepend plugin_name with "tox"!')
        sys.exit(1)


def validate_py_name(which, name):
    matcher = re.compile(r'^[a-z][_a-z0-9]+$')
    if not re.match(matcher, name):
        url = 'https://python.org/dev/peps/pep-0008/#package-and-module-names'
        log.error('%s "%s" not PEP-8 compliant - see %s', which, name, url)
        log.info('Must match %s', matcher.pattern)
        sys.exit(1)


if __name__ == '__main__':
    validate_plugin_name('{{cookiecutter.plugin_name}}')
    validate_py_name('pkg_name', '{{cookiecutter.pkg_name}}')
    validate_py_name('module_name', '{{cookiecutter.module_name}}')
