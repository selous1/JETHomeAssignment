import unittest
import sys
import os
from unittest.mock import patch
from io import StringIO
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.utils.utils import print_table_data, remove_whitespace
from assets.emoji_assets import emojis

class TestPrintTableData(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        class_name = cls.__name__
        print(f"{emojis['gear']} Starting {class_name}...")
    
    def setUp(self):
        print("In method", self._testMethodName)
        self.test_table = [
            [1, "Restaurant A", "Italian", 4.5, "123 Test St"],
            [2, "Restaurant B", "Chinese", 4.2, "456 Example Rd"]
        ]
        self.headers = ["N", "Name", "Cuisines", "Rating", "Address"]
        self.limit = 2
        self.postcode = "12345"
        self.city = "Test City"
    
    # Test case: valid table data
    def test_valid_data(self):
        msg = f"""
                {emojis['sushi']} Data from 2 restaurants with UK postcode 12345 in Test City\n
                N  Name          Cuisines    Rating    Address
                ---  ------------  ----------  --------  --------------
                1  Restaurant A  Italian     4.5       123 Test St
                2  Restaurant B  Chinese     4.2       456 Example Rd
              """
        expected_output = remove_whitespace(msg)
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print_table_data(self.test_table, self.limit, self.postcode, self.city, self.headers)
            output = remove_whitespace(mock_stdout.getvalue())

        self.assertEqual(output, expected_output)
    
    # Test case: empty tamble
    def test_empty_table(self):
        self.table = []
        expected_output = remove_whitespace(f"{emojis['sleepingSymbol']} No data to print.")
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print_table_data([], self.limit, self.postcode, self.city, self.headers)
            output = remove_whitespace(mock_stdout.getvalue())

        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main(verbosity=1)
