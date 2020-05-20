"""Some helper utilities
"""
import re
import inspect
import functools

# regex pattern for converting camel to snake case
camel_to_snake_pattern = re.compile(r"[0-9A-Z](?:[A-Z]*(?![a-z])|[a-z]*)")


def camel_to_snake(string):
    """Convert CamelCase input to snake_case output"""
    if not any(x.isupper() for x in string):
        return string
    return "_".join(g.lower() for g in camel_to_snake_pattern.findall(string))


def rgetattr(obj, attr, *args):
    """Recursive attribute getter for easier nested component access"""

    def _getattr(obj, attr):
        return getattr(obj, attr, *args)

    return functools.reduce(_getattr, [obj] + attr.split("."))


def component_repr(cls):
    """Basic repr based on inspecting kwargs from init of class"""
    parameters = inspect.signature(cls.__init__).parameters
    parameters_string = ", ".join(f"{p}={getattr(cls, p)}" for p in parameters)
    return f"{type(cls).__name__}({parameters_string})"
