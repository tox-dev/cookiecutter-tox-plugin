#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='tox-{{cookiecutter.plugin_name}}',
    description='{{cookiecutter.short_description}}',
    long_description=read('README.rst'),
    version='{{cookiecutter.version}}',
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    maintainer='{{cookiecutter.full_name}}',
    maintainer_email='{{cookiecutter.email}}',
    url='https://github.com/{{cookiecutter.github_username}}/tox-{{cookiecutter.plugin_name}}',
    packages=find_packages(),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=['tox>={{cookiecutter.tox_version}}'],
    entry_points={'tox': ['{{cookiecutter.plugin_name}} = {{cookiecutter.entry_point}}']},
    license='{{cookiecutter.license}}',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        {% if cookiecutter.license == "MIT" -%}
        'License :: OSI Approved :: MIT License',
        {%- elif cookiecutter.license == "BSD-3" -%}
        'License :: OSI Approved :: BSD License',
        {%- elif cookiecutter.license == "GNU GPL v3.0" -%}
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        {%- elif cookiecutter.license == "Apache Software License 2.0" -%}
        'License :: OSI Approved :: Apache Software License',
        {%- elif cookiecutter.license == "Mozilla Public License 2.0" -%}
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        {%- endif %}
    ],
)
