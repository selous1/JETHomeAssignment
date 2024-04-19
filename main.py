import argparse
from src.restaurants import app
from assets.emoji_assets import emojis

PARSER_DESCRIPTION = "Retrieve a number of restaurants data from an UK postcode"
DEFAULT_LIMIT = 10
PARSER_LIMIT_HELP = "set the limit of restaurants to be retrieved"
DEFAULT_POSTCODE = "EC4M7RF"
PARSER_POSTCODE_HELP = "set an UK postcode"

def main():
    # Setup parser and get arguments
    indent_formatter = lambda prog: argparse.RawTextHelpFormatter(prog, max_help_position=40)
    parser = argparse.ArgumentParser(formatter_class=indent_formatter, description=PARSER_DESCRIPTION)
    parser.add_argument("-l", "--limit", type=int, nargs="?", const=DEFAULT_LIMIT, default=DEFAULT_LIMIT, help=PARSER_LIMIT_HELP)
    parser.add_argument("-p", "--postcode", type=str, nargs="?", const=DEFAULT_POSTCODE, default=DEFAULT_POSTCODE, help=PARSER_POSTCODE_HELP)
    
    args = parser.parse_args()    
    limit = args.limit
    postcode = args.postcode
    print(f"{emojis['rocket']} Getting data from {limit} restaurants in postcode {postcode}...\n")

    # Print restaurants data
    app.get_restaurants_data(limit, postcode)

if __name__ == "__main__":
    main()