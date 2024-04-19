from tabulate import tabulate
from io import StringIO
import sys

def print_table_data(table: list, limit: int, postcode: str, city: str, 
                     headers: list = None, floatfmt: str = ".1f", data: str = "restaurants"):
    if not table or limit == 0:
        print("No data to print.")
        return
        
    print(f"Data from {limit} {data} with UK postcode {postcode} in {city}")
    print(tabulate(table, headers, floatfmt=floatfmt))

def list_to_sorted_string(input: list, param: str, delimiter: str) -> str:
    sorted_input = sorted([item[param] for item in input])
    return delimiter.join(sorted_input)

def remove_whitespace(s: str) -> str:
    return s.strip().replace("\t", "").replace(" ", "")

def set_stdout() -> StringIO:
    captured_output = StringIO()
    sys.stdout = captured_output
    return sys.stdout

def get_stdout(captured_output) -> any:
    return captured_output.getvalue().strip()

def reset_stdout() -> None:
    sys.stdout = sys.__stdout__

