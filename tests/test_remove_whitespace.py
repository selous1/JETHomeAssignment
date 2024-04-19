import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.utils.utils import remove_whitespace
from assets.emoji_assets import emojis

class TestRemoveWhitespace(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        class_name = cls.__name__
        print(f"{emojis['gear']} Starting {class_name}...")

    def setUp(self):
        print("In method", self._testMethodName)

    # Test case: Remove whitespace
    def test_remove_whitespace_leading_trailing(self): 
        expected_output = "hello"
        output = remove_whitespace("  hello  ")
        self.assertEqual(expected_output, output)

    # Test case: Remove tabs
    def test_remove_whitespace_leading_trailing_tabs(self): 
        expected_output = "world"
        output = remove_whitespace("\t\tworld\t\t")
        self.assertEqual(expected_output, output)

    # Test case: Remove spaces
    def test_remove_whitespace_all_spaces(self):
        expected_output = "removeallspaces"
        output = remove_whitespace("remove all spaces")
        self.assertEqual(expected_output, output)

    # Test case: Remove all whitespace
    def test_remove_whitespace_all_whitespace(self):
        expected_output = ""
        output = remove_whitespace(" \t \n \r ")
        self.assertEqual(expected_output, output)

if __name__ == "__main__":
    unittest.main(verbosity=1)



