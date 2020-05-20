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

    def test_rgetattr(self):
        """test for recursive getter"""

        class A:
            def __init__(self, b):
                self.b = b

        class B:
            def __init__(self, c):
                self.c = c

        class C:
            def __init__(self, data):
                self.data = data

        for data in ("test", 1, 2.0, True):
            obj = A(B(C(data)))
            self.assertEqual(execs_utils.rgetattr(obj, "b.c.data"), data)

        with self.assertRaises(AttributeError):
            execs_utils.rgetattr(A(B(C("hello"))), "b.fail.data")

    def test_component_repr(self):
        """test introspective component repr"""
        class A:
            def __init__(self, x=None, test=None, another=None):
                self.x = x
                self.test = test
                self.another = another

        A.__repr__ = execs_utils.component_repr

        for x, test, another in ((None, None, None), (1.0, True, "hello")):
            a = self.assertEqual(f"{A(x=x, test=test, another=another)}",
                                 f"A(x={x}, test={test}, another={another})")    
