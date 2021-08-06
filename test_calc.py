import unittest
import calc


class TestCalc(unittest.TestCase):
   
    """funcs need to start with test_"""
    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)