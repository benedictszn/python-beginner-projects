# project: weather checker
# type in a city and get the current weather. it uses open-meteo, a free weather service that needs no sign up
# note: need an internet connection for this one

import json
import urllib.parse
import urllib.request
import urllib.error

# the two web addresses we ask for information
CITY_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

# the weather service sends a number, this turns it into words
WEATHER_CODES = {
    0: "clear sky",
    1: "mostly clear",
    2: "partly cloudy",
    3: "overcast",
    45: "fog",
    51: "light drizzle",
    61: "light rain",
    63: "rain",
    65: "heavy rain",
    71: "light snow",
    73: "snow",
    75: "heavy snow",
    80: "rain showers",
    95: "thunderstorm",
}


def get_data(url, settings):
    # builds the full web address, asks for the data and returns it as a dictionary
    full_url = url + "?" + urllib.parse.urlencode(settings)
    with urllib.request.urlopen(full_url, timeout=10) as response:
        return json.load(response)


def find_city(name):
    # turns a city name into a latitude and longitude
    data = get_data(CITY_URL, {"name": name, "count": 1})

    # if nothing was found there will be no "results" in the data
    if "results" not in data:
        return None
    return data["results"][0]


def show_weather(city_name):
    try:
        city = find_city(city_name)
        if city is None:
            print("sorry, could not find that city")
            return

        weather = get_data(WEATHER_URL, {
            "latitude": city["latitude"],
            "longitude": city["longitude"],
            "current": "temperature_2m,wind_speed_10m,weather_code",
        })
    except urllib.error.URLError:
        # this happens if there is no internet
        print("could not connect, please check your internet")
        return

    now = weather["current"]
    description = WEATHER_CODES.get(now["weather_code"], "unknown")

    print()
    print("weather in", city["name"] + ":")
    print("  temperature:", now["temperature_2m"], "°C")
    print("  conditions:", description)
    print("  wind speed:", now["wind_speed_10m"], "km/h")


def main():
    while True:
        city_name = input("\nenter a city (or just press enter to quit): ").strip()

        # an empty answer means the user wants to stop
        if city_name == "":
            print("bye!")
            break

        show_weather(city_name)


if __name__ == "__main__":
    main()
