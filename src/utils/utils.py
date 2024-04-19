from tabulate import tabulate

def print_table_data(table: list, limit: int, postcode: str, city: str, 
                     headers: list = None, floatfmt: str = ".1f", data: str = "restaurants"):
    if not table or limit == 0:
        print("No data to print.")
        return
        
    print(f"Data from {limit} {data} with UK postcode {postcode} in {city}")
    print(tabulate(table, headers, floatfmt=floatfmt))

def list_to_sorted_string(input: list, param: str, delimiter: str) -> str:
    try:
        sorted_input = sorted([item[param] for item in input])
        sorted_string = delimiter.join(sorted_input)
        return sorted_string
    except Exception as e:
        print(f"Failed to get sorted string: {e}")
        return ""

def remove_whitespace(s: str) -> str:
    return s.strip().replace("\t", "").replace(" ", "")