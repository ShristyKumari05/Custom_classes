import unittest
from custom_classes.rectangle import Rectangle

class RectangleTests(unittest.TestCase):
    def test_iteration(self):
        rect = Rectangle(10, 20)
        result = [item for item in rect]
        expected = [{'length': 10}, {'width': 20}]
        self.assertEqual(result, expected)