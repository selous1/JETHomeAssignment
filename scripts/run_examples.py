import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.restaurants.app import get_restaurants_data
from src.utils.utils import print_separator
from assets.emoji_assets import emojis

def main():
    # Setup
    examples = [
        {"limit": 10, "postcode": "EC4M7RF"},
        {"limit": 2,  "postcode": "SW1A1AA"},
        {"limit": 3,  "postcode": "EH11BE"},
        {"limit": 0,  "postcode": "EC4M7RF"},
        {"limit": 10, "postcode": "A"}
    ]  

    # Run examples
    print(f"{emojis['runner']} Running examples...")
    print_separator()
    for i, example in enumerate(examples, start=1):
        limit, postcode = example["limit"], example["postcode"]
        print(f"{emojis['electricLightBulb']} #{i} Example:")
        print(f"{emojis['hammerAndWrench']}  Limit: {limit} | Postcode: {postcode}\n")
        get_restaurants_data(limit, postcode)
        print_separator()

    print(f"{emojis['partyPopper']} Examples completed!")

if __name__ == "__main__":
    main()
