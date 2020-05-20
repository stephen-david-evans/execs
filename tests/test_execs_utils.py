"""Unit tests for utilities
"""
import unittest
from execs import execs_utils

class TestUtils(unittest.TestCase):
    """Unit tests for utils"""

    def test_camel_to_snake(self):
        """test camel to snake case"""
        self.assertEqual(execs_utils.camel_to_snake("CamelCase"), "camel_case")