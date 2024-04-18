import sys, os, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.restaurants.app import valid_arguments
from utils.utils import set_stdout, reset_stdout, get_stdout

DEFAULT_LIMIT = 10
DEFAULT_POSTCODE = "EC4M7RF"

class TestValidArguments(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Starting tests for TestValidArguments class...")

    @classmethod
    def tearDownClass(cls):
        print("Tests for TestValidArguments completed.")
        print("----------------------------------")

    def setUp(self):
        print("In method", self._testMethodName)
        self.output = set_stdout()
        self.data = {"metaData": {"resultCount": DEFAULT_LIMIT}}
        self.limit = DEFAULT_LIMIT
        self.postcode = DEFAULT_POSTCODE

    def tearDown(self):
        reset_stdout()

    # Test case: valid arguments
    def test_valid_arguments(self):
        self.assertTrue(valid_arguments(self.limit, self.postcode, self.data))

    # Test case: limit is 0
    def test_limit_zero(self):
        msg = "Failed to retrieve restaurants data: Limit is 0. Please insert a valid limit."
        self.assertFalse(valid_arguments(0, self.postcode, self.data))
        self.assertEqual(get_stdout(self.output), msg)

    # Test case: limit exceeds number of restaurants in postcode
    def test_exceeding_limit(self):
        self.data["metaData"]["resultCount"] = self.limit - 1
        msg = f"Failed to retrieve restaurants data: Limit {self.limit} exceeds the number of restaurants {self.limit - 1} in the postcode {self.postcode}."
        self.assertFalse(valid_arguments(self.limit, self.postcode, self.data))
        self.assertEqual(get_stdout(self.output), msg)

    # Test case: invalid postcode
    def test_invalid_postcode(self):
        self.data["metaData"]["resultCount"] = 0
        self.postcode = "A"
        msg = f"Failed to retrieve restaurants data: Nonexistent postcode {self.postcode}. Please insert a valid postcode."
        self.assertFalse(valid_arguments(DEFAULT_LIMIT, self.postcode, self.data))
        self.assertEqual(get_stdout(self.output), msg)

if __name__ == "__main__":
    unittest.main()


