from dotenv import load_dotenv
from pprint import pprint
import requests
import os
import sys

load_dotenv()

def get_current_weather(city="Port Elizabeth"):


    # request_url = f'http://api.openweathermap.org/data/2.5/weather?appof={os.getenv("API_KEY")}&q={city}&units=imperial'

    request_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={os.getenv("API_KEY")}'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n*** Get Current Weatehr Conditions ***\n')

    city = input("Please enter a city name: ")

    if not bool(city.strip()):
        city = "Port Elizabeth"

    weather_data = get_current_weather(city)

    pprint(weather_data)