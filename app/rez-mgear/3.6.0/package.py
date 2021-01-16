# -*- coding:utf-8 -*-

late = globals()["late"]

name = "mgear"
version = "3.6.0"
description = "mgear download"

build_command = "python {root}/rezbuild.py {install}"
private_build_requires = ["rezutil-1"]


def commands():
    env = globals()["env"]
    env.MAYA_MODULE_PATH.append("{root}/payload/release")