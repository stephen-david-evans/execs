"""Some helper utilities
"""
import re

# regex pattern for converting camel to snake case
camel_to_snake_pattern = re.compile(r"[A-Z](?:[A-Z]*(?![a-z])|[a-z]*)")


def camel_to_snake(x):
    """Convert CamelCase input to snake_case output"""
    return "_".join(g.lower() for g in camel_to_snake_pattern.findall(x))


def rgetattr(obj, attr, *args):
    """Recursive attribute getter for easier nested component access"""

    def _getattr(obj, attr):
        return getattr(obj, attr, *args)

    return functools.reduce(_getattr, [obj] + attr.split("."))
