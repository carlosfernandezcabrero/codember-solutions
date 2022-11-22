import unittest

from main import main

test_data: list[dict[str, list[str] | str]] = [
    {
        "input": ["red", "blue", "red", "blue", "green"],
        "output": "['red', 'blue', 'red', 'blue', 'green'] -> 4, blue",
    },
    {
        "input": ["green", "red", "blue", "gray"],
        "output": "['green', 'red', 'blue', 'gray'] -> 2, gray",
    },
    {
        "input": ["blue", "blue", "blue", "blue"],
        "output": "['blue', 'blue', 'blue', 'blue'] -> 1, blue",
    },
    {
        "input": ["red", "green", "red", "green", "red", "green"],
        "output": "['red', 'green', 'red', 'green', 'red', 'green'] -> 6, green",
    },
    {
        "input": ["blue", "red", "blue", "red", "gray"],
        "output": "['blue', 'red', 'blue', 'red', 'gray'] -> 4, red",
    },
    {
        "input": ["red", "red", "blue", "red", "red", "red", "green"],
        "output": "['red', 'red', 'blue', 'red', 'red', 'red', 'green'] -> 3, red",
    },
    {
        "input": ["red", "blue", "red", "green", "red", "green", "red", "green"],
        "output": "['red', 'blue', 'red', 'green', 'red', 'green', 'red', 'green'] -> 6, green",
    },
]


class TestChallenge(unittest.TestCase):
    def test_challenge(self):
        for data in test_data:
            self.assertEqual(main(list(data["input"])), data["output"])
