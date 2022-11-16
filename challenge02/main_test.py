import unittest

from main import main


class TestChallenge(unittest.TestCase):
    def test_challenge(self):
        expected = "thanks for playing codember please share"
        actual = main()
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
