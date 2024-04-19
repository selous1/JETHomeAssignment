import unittest
import sys
import os
from unittest.mock import patch
from io import StringIO
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.restaurants.app import get_restaurant_data

class TestGetRestaurantData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        class_name = cls.__name__
        print(f"Starting {class_name}...")

    def setUp(self):
        print("In method", self._testMethodName)
        self.restaurant_data = {
            "name": "Test Restaurant",
            "cuisines": [{"name": "Italian"}, {"name": "Pizza"}],
            "rating": {"starRating": 4.5},
            "address": {"firstLine": "123 Test St", "postalCode": "12345", "city": "Test City"}
        }

    # Test case: valid restaurant data
    def test_valid_input(self):
        expected_output = ["Test Restaurant", "Italian, Pizza", "4.5", "123 Test St, 12345", "Test City"]
        output = get_restaurant_data(self.restaurant_data)
        self.assertEqual(output, expected_output)
    
    # Test case: missing restaurant data
    def test_missing_data(self):
        self.restaurant_data = {"name": "Test Restaurant", "cuisines": [], "rating": {}}
        expected_output = []
        msg = "Failed to retrieve restaurant data: 'starRating'"
        with unittest.mock.patch("sys.stdout", new=StringIO()) as mock_stdout:
            output = get_restaurant_data(self.restaurant_data)
            stdout = mock_stdout.getvalue().strip()

        self.assertEqual(output, expected_output)
        self.assertEqual(stdout, msg)
        
if __name__ == "__main__":
    unittest.main(verbosity=1)


