
# weather_api.py
import requests

API_KEY = "your_api_key_here"  # Get from openweathermap.org
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

city = input("Enter city name: ")
url = BASE_URL + "appid=" + API_KEY + "&q=" + city

response = requests.get(url).json()

if response["cod"] != "404":
    weather = response["main"]
    temp = round(weather["temp"] - 273.15, 2)
    humidity = weather["humidity"]
    desc = response["weather"][0]["description"]

    print(f"🌍 City: {city}")
    print(f"🌡 Temperature: {temp}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"☁ Weather: {desc}")
else:
    print("❌ City not found!")
