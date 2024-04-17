from src.restaurants import app

LIMIT = 10

if __name__ == "__main__":
    # Setup

    # Print restaurants data
    app.get_restaurant_data(LIMIT)