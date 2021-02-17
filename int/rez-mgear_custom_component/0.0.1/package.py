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

_environ = {
    "MGEAR_SHIFTER_COMPONENT_PATH": [
        "{root}/payload/component"
    ],
    # "MGEAR_SHIFTER_CUSTOMSTEP_PATH": {
    #     "{root}/python/mGear/build/custom_steps"
    # },
    # "MGEAR_SYNOPTIC_PATH": "{root}/python/mGear/env/synoptic",
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