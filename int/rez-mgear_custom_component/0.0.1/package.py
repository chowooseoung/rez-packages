# -*- coding:utf-8 -*-

late = globals()["late"]

name = "mgear_custom_component"
version = "0.0.1"
description = "mgear custom component download"

build_command = "python {root}/rezbuild.py {install}"
private_build_requires = ["rezutil-1", "python"]

requires = [
    # Dependencies
    "mgear",
]

def commands():
    env = globals()["env"]
    env.MGEAR_SHIFTER_COMPONENT_PATH.append("{root}/payload/component")