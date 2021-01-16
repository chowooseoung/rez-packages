# -*- coding:utf-8 -*-

name = "create_proj"
version = "1.0.1"
requires = [
    "python",
]

private_build_requires = ["rezutil-1"]
build_command = "python -m rezutil build {root}"

category = "int"


def commands():
    env = globals()["env"]
    alias = globals()["alias"]

    # For Windows
    env.PATH.prepend("{root}/bin")

    # For Unix
    alias("create", "python {root}/bin/create.py")
