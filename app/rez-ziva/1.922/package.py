# -*- coding:utf-8 -*-

name = "ziva"
version = "1.922"

build_command = "python -m rezutil build {root}"
private_build_requires = ["python-2.7+<4", "rezutil-1"]

_environ = {
    "MAYA_MODULE_PATH": [
        "{root}/ziva"
    ],
}


def commands():
    env = globals()["env"]
    this = globals()["this"]
    expandvars = globals()["expandvars"]

    _environ = this._environ

    for key, value in _environ.items():
        if isinstance(value, (tuple, list)):
            [env[key].append(expandvars(v)) for v in value]
        else:
            env[key] = expandvars(value)