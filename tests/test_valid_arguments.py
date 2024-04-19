import unittest
import sys
import os
from unittest.mock import patch
from io import StringIO
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.restaurants.app import valid_arguments
from assets.emoji_assets import emojis

DEFAULT_LIMIT = 10
DEFAULT_POSTCODE = "EC4M7RF"

class TestValidArguments(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        class_name = cls.__name__
        print(f"{emojis['gear']} Starting {class_name}...")

    def setUp(self):
        print("In method", self._testMethodName)
        self.number_of_restaurants = DEFAULT_LIMIT
        self.limit = DEFAULT_LIMIT
        self.postcode = DEFAULT_POSTCODE

    # Test case: valid arguments
    def test_valid_arguments(self):
        self.assertTrue(valid_arguments(self.limit, self.postcode, self.number_of_restaurants))

    # Test case: limit exceeds number of restaurants in postcode
    def test_exceeding_limit(self):
        self.number_of_restaurants -= 1
        self.assertTrue(valid_arguments(self.limit, self.postcode, self.number_of_restaurants))

    # Test case: limit is 0
    def test_limit_zero(self):
        msg = f"{emojis['collisionSymbol']} Failed to retrieve restaurants data: Please insert a valid limit."
        with unittest.mock.patch("sys.stdout", new=StringIO()) as mock_stdout:
            output = valid_arguments(0, self.postcode, self.number_of_restaurants)
            stdout = mock_stdout.getvalue().strip()

        self.assertFalse(output)
        self.assertEqual(stdout, msg)

    # Test case: invalid postcode
    def test_invalid_postcode(self):
        self.number_of_restaurants = 0
        self.postcode = "A"
        msg = f"{emojis['collisionSymbol']} Failed to retrieve restaurants data: Nonexistent postcode {self.postcode}. Please insert a valid postcode."
        with unittest.mock.patch("sys.stdout", new=StringIO()) as mock_stdout:
            output = valid_arguments(DEFAULT_LIMIT, self.postcode, self.number_of_restaurants)
            stdout = mock_stdout.getvalue().strip()

        self.assertFalse(output)
        self.assertEqual(stdout, msg)

if __name__ == "__main__":
    unittest.main(verbosity=1)



