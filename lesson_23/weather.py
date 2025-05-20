from dotenv import load_dotenv
import os
from pprint import pprint
import requests

load_dotenv()


def get_current_weather(city="São Paulo"):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print("\n**** Get Current Weather Conditions ****\n")
    city = input("Please, enter a city name:\n")

    # Check for empty strings or with only white spaces
    if not bool(city.strip()):
        city = "São Paulo"

    weather_data = get_current_weather(city)

    print("")
    pprint(weather_data)
