import unittest
import sys
import os
import io
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from unittest.mock import patch
from urllib3.response import HTTPResponse
from src.restaurants.app import get_restaurants_data
from src.utils.utils import remove_whitespace
from assets.emoji_assets import emojis

DEFAULT_LIMIT = 1
DEFAULT_POSTCODE = "12345"

class TestGetRestaurantsData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        class_name = cls.__name__
        print(f"{emojis['gear']} Starting {class_name}...")

    def setUp(self):
        print("In method", self._testMethodName)
        self.limit = DEFAULT_LIMIT
        self.postcode = DEFAULT_POSTCODE
    
    # Test case: valid restaurant data
    @patch('urllib3.PoolManager.request')
    def test_valid_data(self, mock_request):
        # Mock API response
        mock_response_data = (
            b'{"metaData": {"resultCount": 1}, '
            b'"restaurants": [{"name": "Test Restaurant", '
            b'"cuisines": [{"name": "Italian"}, {"name": "Pizza"}], '
            b'"rating": {"starRating": 4.5}, '
            b'"address": {"firstLine": "123 Test St", '
            b'"postalCode": "12345", "city": "Test City"}}]}')
        mock_response = HTTPResponse(body=mock_response_data)
        mock_request.return_value = mock_response
        
        msg = f"""{emojis['sushi']} Data from 1 restaurants with UK postcode 12345 in Test City\n
                    N  Name             Cuisines          Rating  Address
                  ---  ---------------  --------------  --------  ------------------
                    1  Test Restaurant  Italian, Pizza       4.5  123 Test St, 12345"""
        expected_output = remove_whitespace(msg)
        with patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            get_restaurants_data(self.limit, self.postcode)
            output = remove_whitespace(mock_stdout.getvalue())
        
        self.assertEqual(output, expected_output)
    
if __name__ == "__main__":
    unittest.main(verbosity=1)


