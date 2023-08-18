import tkinter as tk
from tkinter import messagebox
import requests

class WeatherAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Wetter-App")

        self.city_entry = tk.Entry(self.root)
        self.city_entry.pack(padx=10, pady=5)

        self.get_weather_button = tk.Button(self.root, text="Wetter abrufen", command=self.get_weather)
        self.get_weather_button.pack(padx=10, pady=5)

        self.weather_label = tk.Label(self.root, text="", wraplength=300)
        self.weather_label.pack(padx=10, pady=5)

    def get_weather(self):
        city_name = self.city_entry.get()
        if city_name:
            weather_data = self.fetch_weather_data(city_name)
            if weather_data:
                temperature, humidity, description = weather_data
                weather_text = (
                    f"Wetter in {city_name}:\n"
                    f"Temperatur: {temperature}°C\n"
                    f"Luftfeuchtigkeit: {humidity}%\n"
                    f"Beschreibung: {description}"
                )
                self.weather_label.config(text=weather_text)
        else:
            messagebox.showwarning("Fehler", "Bitte geben Sie den Stadtnamen ein.")

    def fetch_weather_data(self, city_name):
        url = "https://weatherapi-com.p.rapidapi.com/current.json"
        querystring = {"q": city_name}
        headers = {
            "X-RapidAPI-Key": "e9f2824844mshc1c978f851f7e8cp1c72f2jsn9da392e99904",
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        if "current" in data:
            current_data = data["current"]
            temperature = current_data["temp_c"]
            humidity = current_data["humidity"]
            description = current_data["condition"]["text"]
            return temperature, humidity, description
        else:
            messagebox.showerror("Fehler", "Stadt nicht gefunden.")
            return None

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherAppGUI(root)
    root.mainloop()
