import urllib.request, json
from utils import utils

URL = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/"
TABLE_HEADERS = ["N","Name","Cuisines","Rating","Address"]
TABLE_FLOAT = ".1f"
TABLE_TYPE = "restaurants"

def get_restaurants_data(limit: int, postcode: str) -> None:
    request_url = f"{URL}{postcode}"
    try:
        # Get data from API    
        response = urllib.request.urlopen(request_url)
        data = json.loads(response.read())

        # Verify arguments
        number_of_restaurants = data["metaData"]["resultCount"]
        if not valid_arguments(limit, postcode, number_of_restaurants):
            return
        
        limit = min(limit, number_of_restaurants)
        restaurants_data = []
        restaurants = data["restaurants"]
        for i in range(limit):
            # Get data from each restaurant
            restaurant = restaurants[i]
            name, cuisines, rating, address, city = get_restaurant_data(restaurant)
       
            # Add restaurant data to output table
            restaurant_entry = [i + 1, name, cuisines, rating, address]
            restaurants_data.append(restaurant_entry)

        # Print output table
        utils.print_table_data(restaurants_data, limit, postcode, city, TABLE_HEADERS, TABLE_FLOAT, TABLE_TYPE)
        
    except Exception as e:
        print(f"Failed to retrieve restaurants data: {e}")
        return

    return

def valid_arguments(limit, postcode, number_of_restaurants) -> bool:
    if limit <= 0:
        print(f"Failed to retrieve restaurants data: Please insert a valid limit.")
        return False
    if number_of_restaurants == 0:
        print(f"Failed to retrieve restaurants data: Nonexistent postcode {postcode}. Please insert a valid postcode.")
        return False

    return True

def get_restaurant_data(restaurant: dict) -> list:
    try:
        name = restaurant["name"]
        cuisines = utils.list_to_sorted_string(restaurant["cuisines"], "name", ", ")
        rating = str(restaurant["rating"]["starRating"])
        city = restaurant["address"]["city"]
        address = f"""{restaurant["address"]["firstLine"]}, {restaurant["address"]["postalCode"]}"""
        return [name, cuisines, rating, address, city]

    except Exception as e:
        print(f"Failed to retrieve restaurant data: {e}")
        return []