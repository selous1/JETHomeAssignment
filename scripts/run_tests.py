import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.utils.utils import print_separator
from assets.emoji_assets import emojis

def run_tests():
    print(f"{emojis['rocket']} Starting test suite...")
    print_separator()
    test_suite = unittest.defaultTestLoader.discover(start_dir="tests", pattern="test_*.py")
    unittest.TextTestRunner().run(test_suite)

if __name__ == "__main__":
    run_tests()
