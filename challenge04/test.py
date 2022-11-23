import unittest

from script import main_function


class Test(unittest.TestCase):
    def test(self):
        actual = main_function()

        self.assertEqual(len(actual), 165)
        self.assertEqual(actual[55], "23555")
