# -*- coding: utf-8 -*-

late = globals()["late"]

name = 'rezutil'
version = '1.5.0'

build_command = "python {root}/install.py"
private_build_requires = ["python-2.7+<4"]


def commands():
    env = globals()["env"]
    env.PYTHONPATH.prepend("{root}/python")