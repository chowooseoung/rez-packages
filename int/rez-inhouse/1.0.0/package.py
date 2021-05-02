# -*- coding:utf-8 -*-

"""
환경변수나 하드코딩이 필요한것들.
"""

name = "inhouse"
version = "1.0.0"
author = "chowooseoung"

_environ = {
    "any": {
        "PROJECTS_PATH": "D:/pipeline/projects", 
        "INHOUSE_PATH": "D:/pipeline/inhouse",
        "INHOUSE_MAYA_PATH": "D:/pipeline/inhouse/DCC/maya",

        "INHOUSE_MONGO": "localhost:27017",
    },

    "maya": {
        # "MAYA_SHELF_PATH": "{env.PROJECT_PATH}/maya/shelves",
        "XBMLANGPATH": [
            "{env.INHOUSE_MAYA_PATH}/icons"
        ]
    }
}

environ_ = {
    "any": {

    },

    "maya": {
        "MAYA_MODULE_PATH": [
            r"D:\pipeline\inhouse\DCC\maya\ext\modules\animation",
            r"D:\pipeline\inhouse\DCC\maya\ext\modules\common",
            r"D:\pipeline\inhouse\DCC\maya\ext\modules\modeling",
            r"D:\pipeline\inhouse\DCC\maya\ext\modules\rigging",
            r"D:\pipeline\inhouse\DCC\maya\int\modules\animation",
            r"D:\pipeline\inhouse\DCC\maya\int\modules\common",
            r"D:\pipeline\inhouse\DCC\maya\int\modules\modeling",
            r"D:\pipeline\inhouse\DCC\maya\int\modules\rigging",
        ],

        "MAYA_SCRIPT_PATH": [
            r"D:\pipeline\inhouse\DCC\maya\ext\scripts",
            r"D:\pipeline\inhouse\DCC\maya\int\scripts",
        ],

        "MAYA_PLUG_IN_PATH": [
            r"D:\pipeline\inhouse\DCC\maya\ext\plug-ins\animation",
            r"D:\pipeline\inhouse\DCC\maya\ext\plug-ins\common",
            r"D:\pipeline\inhouse\DCC\maya\ext\plug-ins\modeling",
            r"D:\pipeline\inhouse\DCC\maya\ext\plug-ins\rigging",
            r"D:\pipeline\inhouse\DCC\maya\int\plug-ins\animation",
            r"D:\pipeline\inhouse\DCC\maya\int\plug-ins\common",
            r"D:\pipeline\inhouse\DCC\maya\int\plug-ins\modeling",
            r"D:\pipeline\inhouse\DCC\maya\int\plug-ins\rigging",
        ],
    }
}

build_command = "python -m rezutil build {root}"
private_build_requires = ["python-2.7+<4", "rezutil-1"]


def commands():
    import os

    env = globals()["env"]
    this = globals()["this"]
    request = globals()["request"]
    expandvars = globals()["expandvars"]

    environ = this._environ
    environ_ = this.environ_
    result = list(environ["any"].items())

    # Add request-specific environments
    for key, values in environ.items():
        if key not in request:
            continue

        result += list(values.items())

    for key, values in environ_.items():    
        if key not in request:
            continue
        for k, v in values.items():
            paths = list()
            for path in v:
                if os.path.exists(path):
                    [paths.append(os.path.join(path, x)) for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
            result.append((k, paths))

    for key, value in result:
        if isinstance(value, (tuple, list)):
            [env[key].append(expandvars(v)) for v in value]
        else:
            env[key] = expandvars(value)
