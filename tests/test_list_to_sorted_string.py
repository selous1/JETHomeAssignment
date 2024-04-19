import unittest
import sys
import os
from unittest.mock import patch
from io import StringIO
import unittest.mock
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.utils.utils import list_to_sorted_string

class TestListToSortedString(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        class_name = cls.__name__
        print(f"Starting {class_name}...")

    def setUp(self):
        print("In method", self._testMethodName)
        self.param = "param"
        self.delimiter = ", "

    # Test case: empty list
    def test_empty_list(self):
        expected_output = ""
        output = list_to_sorted_string([], self.param, self.delimiter)
        self.assertEqual(output, expected_output)

    # Test case: list with a single item
    def test_single_item_list(self):
        input_list = [{"param": "value"}]
        expected_output = "value"
        output = list_to_sorted_string(input_list, self.param, self.delimiter)
        self.assertEqual(output, expected_output)

    # Test case: list with multiple items
    def test_multiple_items_list(self):
        input_list = [{"param": "a"}, {"param": "b"}, {"param": "c"}]
        expected_output = "a, b, c"
        output = list_to_sorted_string(input_list, self.param, self.delimiter)
        self.assertEqual(output, expected_output)

    # Test case: list with duplicated items
    def test_duplicate_items_list(self):
        input_list = [{"param": "a"}, {"param": "a"}, {"param": "b"}]
        expected_output = "a, a, b"
        output = list_to_sorted_string(input_list, self.param, self.delimiter)
        self.assertEqual(output, expected_output)

    # Test case: list with missing value
    def test_empty_param(self):
        input_list = [{"param": ""}]
        output = list_to_sorted_string(input_list, self.param, self.delimiter)
        self.assertEqual(output, "")

    # Test case: list with missing parameters
    def test_missing_param(self):
        input_list = [{}]
        expected_output = ""
        msg = "Failed to get sorted string: 'param'"
        with unittest.mock.patch("sys.stdout", new=StringIO()) as mock_stdout:
            output = list_to_sorted_string(input_list, self.param, self.delimiter)
            stdout = mock_stdout.getvalue().strip()

        self.assertEqual(output, expected_output)
        self.assertEqual(stdout, msg)

if __name__ == "__main__":
    unittest.main(verbosity=1)

