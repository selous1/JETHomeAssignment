import urllib3
import time
from src.utils import utils
from assets.emoji_assets import emojis

URL = "http://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/"
TABLE_HEADERS = ["N","Name","Cuisines","Rating","Address"]
TABLE_FLOAT = ".1f"
TABLE_TYPE = "restaurants"

def get_restaurants_data(limit: int, postcode: str) -> None:
    try:
        # Get data from API
        http = urllib3.PoolManager()
        request_url = f"{URL}{postcode}" 
        response = http.request("GET", request_url)
        data = response.json()

        # Verify arguments
        number_of_restaurants = data["metaData"]["resultCount"]
        if not valid_arguments(limit, postcode, number_of_restaurants):
            return
        
        print(f"{emojis['checkMark']} Data found! Retrieving data...\n")
        time.sleep(.2)

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
        return
    except Exception as e:
        print(f"{emojis['collisionSymbol']} Failed to retrieve restaurants data: {e}")
        return

def valid_arguments(limit, postcode, number_of_restaurants) -> bool:
    if limit <= 0:
        print(f"{emojis['collisionSymbol']} Failed to retrieve restaurants data: Please insert a valid limit.")
        return False
    if number_of_restaurants == 0:
        print(f"{emojis['collisionSymbol']} Failed to retrieve restaurants data: Nonexistent postcode {postcode}. Please insert a valid postcode.")
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
        print(f"{emojis['collisionSymbol']} Failed to retrieve restaurant data: {e}")
        return []
    