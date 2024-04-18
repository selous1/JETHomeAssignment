import unittest

def run_tests():
    print("Starting test suite...")
    print("----------------------------------")
    test_suite = unittest.defaultTestLoader.discover(start_dir="tests", pattern="test_*.py")
    unittest.TextTestRunner().run(test_suite)

if __name__ == "__main__":
    run_tests()
