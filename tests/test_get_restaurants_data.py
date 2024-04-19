import unittest
import sys
import os
import io
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from unittest.mock import patch
from src.restaurants.app import get_restaurants_data
from src.utils.utils import remove_whitespace

DEFAULT_LIMIT = 1
DEFAULT_POSTCODE = "12345"

class TestGetRestaurantsData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        class_name = cls.__name__
        print(f"Starting {class_name}...")

    def setUp(self):
        print("In method", self._testMethodName)
        self.limit = DEFAULT_LIMIT
        self.postcode = DEFAULT_POSTCODE
    
    # Test case: valid restaurant data
    @patch("urllib.request.urlopen")
    def test_valid_data(self, mock_urlopen):
        # Mock API response
        mock_response = unittest.mock.Mock()
        mock_response.read.return_value = (b'{"metaData": {"resultCount": 5}, "restaurants": \
            [{"name": "Test Restaurant", "cuisines": [{"name": "Italian"}, {"name": "Pizza"}], \
            "rating": {"starRating": 4.5}, "address": {"firstLine": "123 Test St", "postalCode": "12345", "city": "Test City"}}]}')
        mock_urlopen.return_value = mock_response
        
        expected_output = f"""Data from 1 restaurants with UK postcode 12345 in Test City
                              N  Name             Cuisines          Rating  Address
                            ---  ---------------  --------------  --------  ------------------
                              1  Test Restaurant  Italian, Pizza       4.5  123 Test St, 12345"""
        with patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            get_restaurants_data(self.limit, self.postcode)
            output = mock_stdout.getvalue()
            
        self.assertEqual(remove_whitespace(output), remove_whitespace(expected_output))
    
if __name__ == "__main__":
    unittest.main(verbosity=1)


