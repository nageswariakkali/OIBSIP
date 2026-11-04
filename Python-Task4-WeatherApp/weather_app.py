# Basic Weather App - Beginner Tier
# Oasis Infobyte - Python Programming Track - Task 4

import requests

# 🔑 PASTE YOUR OPENWEATHERMAP API KEY HERE
API_KEY = "f2a5c725c361f9a3fafcbe8868a08b29"


def get_city_name():
    """Keeps asking until the user enters a non-empty city name."""
    while True:
        city = input("Enter city name: ").strip()
        if city == "":
            print("❌ Error: City name cannot be empty. Please try again.\n")
            continue
        return city


def get_weather(city):
    """
    Calls the OpenWeatherMap API and returns the parsed JSON data.
    Handles network errors and invalid city names gracefully.
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # gives temperature in Celsius directly
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if response.status_code == 200:
            return data
        elif response.status_code == 404:
            print(f"\n❌ Error: City '{city}' not found. Please check the spelling.\n")
            return None
        elif response.status_code == 401:
            print("\n❌ Error: Invalid API key. Please check your API key.\n")
            return None
        else:
            print(f"\n❌ Error: Something went wrong (status code {response.status_code}).\n")
            return None

    except requests.exceptions.Timeout:
        print("\n❌ Error: The request timed out. Please check your internet connection.\n")
        return None
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: No internet connection. Please check your network.\n")
        return None


def display_weather(data):
    """Prints the weather details in a readable format."""
    city_name = data["name"]
    country = data["sys"]["country"]
    temp_c = data["main"]["temp"]
    temp_f = (temp_c * 9 / 5) + 32
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"].title()
    wind_speed = data["wind"]["speed"]

    print("\n" + "=" * 40)
    print(f"      WEATHER IN {city_name.upper()}, {country}")
    print("=" * 40)
    print(f"Condition     : {description}")
    print(f"Temperature   : {temp_c:.1f}°C  /  {temp_f:.1f}°F")
    print(f"Humidity      : {humidity}%")
    print(f"Wind Speed    : {wind_speed} m/s")
    print("=" * 40)


def main():
    print("=" * 40)
    print("      WELCOME TO WEATHER APP")
    print("=" * 40)

    city = get_city_name()
    data = get_weather(city)

    if data:
        display_weather(data)


if __name__ == "__main__":
    main()