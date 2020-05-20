"""Unit tests for utilities
"""
import unittest
from execs import execs_utils

class TestUtils(unittest.TestCase):
    """Unit tests for utils"""

    def test_camel_to_snake(self):
        """test camel to snake case"""
        self.assertEqual(execs_utils.camel_to_snake("CamelCase"), "camel_case")
        self.assertEqual(execs_utils.camel_to_snake("CAMELCase"), "camel_case")
        self.assertEqual(execs_utils.camel_to_snake("CAMELCASE"), "camelcase")
        self.assertEqual(execs_utils.camel_to_snake("snake_case"), "snake_case")
        self.assertEqual(execs_utils.camel_to_snake("A1b2C3d"), "a_1b_2c_3d")