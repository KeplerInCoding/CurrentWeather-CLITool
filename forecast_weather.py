# // accepts a city's name and returns the current weather forecast
# //fetch weather data and parse it using Python
# //data parsing, and error handling.
# //API key: 547ce9cae097717245b375ca024431ed
# //API call: api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

import requests
import json
import sys

def weather_forecast(city):
    api_key = "547ce9cae097717245b375ca024431ed"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    # //try Block 
    try:
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            print(" Temperature (in kelvin unit) = " +
                  str(current_temperature) +
                  "\n atmospheric pressure (in hPa unit) = " +
                  str(current_pressure) +
                  "\n humidity (in percentage) = " +
                  str(current_humidity) +
                  "\n description = " +
                  str(weather_description))
        else:
            print(" City Not Found ")
    # //except Block
    except:
        print("Error in the HTTP request")
    





if __name__ == "__main__":
    city = sys.argv[1]
    weather_forecast(city)

# $ python forecast_weather.py "London"
# Temperature (in kelvin unit) = 280.32
# atmospheric pressure (in hPa unit) = 1012
# humidity (in percentage) = 81
# description = light intensity drizzle


