# -*- coding: utf-8 -*-
import logging

from tox import hookimpl

log = logging.getLogger('{{cookiecutter.plugin_name}}')


def tox_addoption(parser):
    parser.add_argument('--my-option', action='store', default="default value", help='my option')


@hookimpl
def tox_configure(config):
    log.info("my option is: '%s'", config.option.my_option)
