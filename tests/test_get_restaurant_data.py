import sys, os, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.restaurants.app import get_restaurant_data
from src.utils.utils import set_stdout, reset_stdout

class TestGetRestaurantData(unittest.TestCase):

    def setUp(self):
        print("In method", self._testMethodName)
        self.restaurant_data = {
            "name": "Test Restaurant",
            "cuisines": [{"name": "Italian"}, {"name": "Pizza"}],
            "rating": {"starRating": 4.5},
            "address": {"firstLine": "123 Test St", "postalCode": "12345", "city": "Test City"}
        }
        self.output = set_stdout()

    def tearDown(self):
        reset_stdout()

    # Test case: valid restaurant data
    def test_valid_input(self):
        expected_output = ["Test Restaurant", "Italian, Pizza", "4.5", "123 Test St, 12345", "Test City"]
        self.assertEqual(get_restaurant_data(self.restaurant_data), expected_output)
    
    # Test case: missing restaurant data
    def test_missing_data(self):
        self.restaurant_data = {"name": "Test Restaurant", "cuisines": [], "rating": {}}
        expected_output = []
        self.assertEqual(get_restaurant_data(self.restaurant_data), expected_output)

if __name__ == "__main__":
    unittest.main(verbosity=2)


