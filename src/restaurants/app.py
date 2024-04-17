import urllib.request, json
from tabulate import tabulate

POSTCODE = "EC4M7RF"
URL = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/"
HEADERS = ["N","Name","Cuisines","Rating","Address"]

def get_restaurant_data(limit: int) -> None:
    request_url = f"{URL}{POSTCODE}"
    try:        
        response = urllib.request.urlopen(request_url)
        data = json.loads(response.read())

        table = []
        restaurants = data["restaurants"]
        # Get data from each restaurant
        for idx in range(limit):
            restaurant = restaurants[idx]
            name = restaurant["name"]
            cuisines_data = restaurant["cuisines"]
            cuisines = ", ".join([cuisine["name"] for cuisine in cuisines_data])
            rating = "{:.1f}".format(restaurant["rating"]["starRating"])
            city = restaurant["address"]["city"]
            first_line = restaurant["address"]["firstLine"]
            postal_code = restaurant["address"]["postalCode"]
            address = f"{first_line}, {postal_code}"
            
            # Add data from restaurant to table
            entry = [idx + 1, name, cuisines, rating, address]
            table.append(entry)

        # Print table with restaurants data
        print(f"Data from {limit} restaurants in {city}")
        print(tabulate(table, HEADERS, floatfmt=".1f"))
        
    except Exception as e:
        print(f"Failed to get restaurants data: {e}")
        return

    return