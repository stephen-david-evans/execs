# Execs: Experimental Entity Component System

## Documentation

Documentation is build using [Sphinx](https://www.sphinx-doc.org/en/master/index.html) - see the Makefile in [docs](docs) for build instructions.

## Testing

To run unit tests (from top level directory):

    python -m unittest discover tests

All tests should be located in [tests](tests) directory, split into tests for different modules using the naming convention: `test_<module>.py`. Tests are implemented using the [unittest](https://docs.python.org/3/library/unittest.html) framework from the standard library.