import shutil
from tabulate import tabulate
from assets.emoji_assets import emojis

def print_table_data(table: list, limit: int, postcode: str, city: str, 
                     headers: list = None, floatfmt: str = ".1f", data: str = "restaurants"):
    if not table:
        print(f"{emojis['sleepingSymbol']} No data to print.")
        return
    print(f"{emojis['sushi']} Printing data from {limit} {data} with postcode {postcode} in {city}...\n")
    print(tabulate(table, headers, floatfmt=floatfmt))

def list_to_sorted_string(input: list, param: str, delimiter: str) -> str:
    try:
        sorted_input = sorted([item[param] for item in input])
        sorted_string = delimiter.join(sorted_input)
        return sorted_string
    except Exception as e:
        print(f"{emojis['collisionSymbol']} Failed to get sorted string: {e}")
        return ""

def remove_whitespace(s: str) -> str:
    return s.strip().replace("\t", "").replace(" ", "")

def read_emoji_assets(file_path: str) -> dict:
    emoji_assets = {}
    with open(file_path, "r") as file:
        for line in file:
            if line and "," in line:
                name, code = line.strip().split(",")
                code = code.encode('utf-8').decode('unicode_escape')
                emoji_assets[name] = code
    return emoji_assets

def print_separator() -> None:
    terminal_width = shutil.get_terminal_size().columns
    width = min(170, terminal_width)
    separator = "-" * width
    print(separator)

def print_getting_data(limit: int, postcode: str) -> None:
    print(f"{emojis['rocket']} Getting data from {limit} restaurants in postcode {postcode}...")

def print_data_found() -> None:
    print(f"{emojis['checkMark']} Data found! Retrieving data...")

def print_insert_valid_limit() -> None:
    print(f"{emojis['collisionSymbol']} Failed to retrieve restaurants data: Please insert a valid limit.")

def print_insert_valid_postcode(postcode: str) -> None:
    print(f"{emojis['collisionSymbol']} Failed to retrieve restaurants data: Nonexistent postcode {postcode}. Please insert a valid postcode.")

def print_failed_restaurant_retrieval(e: Exception) -> None:
    print(f"{emojis['collisionSymbol']} Failed to retrieve restaurant data: {e}")