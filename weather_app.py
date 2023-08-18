import requests

API_KEY = "DEIN_API_SCHLÜSSEL"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

import requests

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"53.1,-0.13"}

headers = {
	"X-RapidAPI-Key": "e9f2824844mshc1c978f851f7e8cp1c72f2jsn9da392e99904",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

def get_weather(city_name):
    complete_url = f"{BASE_URL}q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] == "404":
        print("Stadt nicht gefunden.")
        return None
    
    main_info = data["main"]
    weather_info = data["weather"][0]
    
    temperature = main_info["temp"]
    humidity = main_info["humidity"]
    description = weather_info["description"]
    
    return temperature, humidity, description

if __name__ == "__main__":
    city = input("Geben Sie den Namen der Stadt ein: ")
    weather_data = get_weather(city)
    
    if weather_data:
        temperature, humidity, description = weather_data
        print(f"Wetter in {city}:")
        print(f"Temperatur: {temperature}°C")
        print(f"Luftfeuchtigkeit: {humidity}%")
        print(f"Beschreibung: {description}")
