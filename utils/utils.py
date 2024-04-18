from tabulate import tabulate

def print_table_data(table: list, limit: int, postcode: str, city: str, 
                     headers: list = None, floatfmt: str = ".1f", data: str = "restaurants"):
    if not table:
        print("No table to print.")
        return
        
    print(f"Data from {limit} {data} from postcode {postcode} in {city}")
    print(tabulate(table, headers, floatfmt=floatfmt))

def list_to_sorted_string(input: list, param: str, delimiter: str) -> str:
    sorted_input = sorted([item[param] for item in input])
    return delimiter.join(sorted_input)