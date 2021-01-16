
name = "portfolio"

version = "1.0.0"

category = "proj"

_requires = {
    "any": [
        "avalon",

        "~maya-2020"
    ],

    "maya": [
        "mgear-3.6"
    ],
    "nuke": [],
    "houdini": [],
}

_environ = {
    "any": {
        # PROJECTS_PATH - core_pipeline
        "PROJECT_NAME": "portfolio",
        "PROJECT_PATH": "{env.PROJECTS_PATH}/portfolio", 
    },

    "maya": {
    }
}


build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1"]

late = locals()["late"]


@late()
def requires():
    """Requirements relative a request

    This function merges a the "any" requirements with e.g. "maya"
    if "maya" is part of a request. Normally, every requirement
    is included with every request, but in this case we wouldn't want
    "maya" requirements included for e.g. "nuke" or "houdini" etc.
    The @late decorate makes this function get called at the time
    of calling `rez env` whereby `request` contains the requests
    made during that time.

    """
    global this
    global request
    global in_context
    
    requires = this._requires
    result = requires["any"][:]

    # Add request-specific requirements
    if in_context():
        for name, reqs in requires.items():
            if name not in request:
                continue

            result += reqs

    return result


def commands():
    env = globals()["env"]
    this = globals()["this"]
    request = globals()["request"]
    expandvars = globals()["expandvars"]

    environ = this._environ
    result = list(environ["any"].items())

    # Add request-specific environments
    for key, values in environ.items():
        if key not in request:
            continue

        result += list(values.items())

    for key, value in result:
        if isinstance(value, (tuple, list)):
            [env[key].append(expandvars(v)) for v in value]
        else:
            env[key] = expandvars(value)
