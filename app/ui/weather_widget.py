from pathlib import Path
import tkinter as tk
from ui.image_loader import make_icon

class weatherWidget():
    def __init__(self, parent, service):
        self.parent = parent
        self.service = service

        self.frame = tk.Frame(self.parent, bg="#101820", borderwidth=2, relief="solid")
        self.frame.pack(fill=tk.X, padx=10, pady=10)
        self.frame.config(highlightthickness=0, bd=0)

        #Region temperature icon and label
        self.temperature_icon = make_icon("app/ui/icons/thermometer.svg", color="#fffff0", size=(30, 30), output_path="app/ui/icons/thermometer.png")  # Default icon
        self.temperature_icon_label = tk.Label(
            self.frame,
            image=self.temperature_icon,
            bg="#101820",
        )
        self.temperature_icon_label.pack(side=tk.LEFT, padx=10, pady=10)
        #endregion temperature icon and label


        #region weather icon and label
        self.weather_label = tk.Label(
            self.frame,
            text="Weather",
            font=("DejaVu Sans", 12, "bold"),
            fg="#fffff0",
            bg="#101820",
        )
        self.weather_label.pack(side=tk.LEFT, padx=10, pady=10)
        #endregion weather icon and label

        #region weather icon
        weather_icon = make_icon("app/ui/icons/sun.svg", color="#fffff0", size=(30, 30), output_path="app/ui/icons/day.png")
        self.weather_icon_label = tk.Label(
            self.frame,
            image=weather_icon,
            bg="#101820",
        )
        self.weather_icon_label.pack(side=tk.RIGHT, padx=10, pady=10)
        #endregion weather icon

        self.update_weather()

        

    def update_weather(self):
        weather = self.service.fetch()
        self.weather_label.config(text=f"{weather['temperature']}°F")
        
        # Get filename from DetermineWeatherIcon
        icon_svg = self.DetermineWeatherIcon(weather['weathercode'])
        icon_path = Path(__file__).parent / "icons" / icon_svg
        make_icon(str(icon_path), color="#fffff0", size=(30, 30), output_path="app/ui/icons/weather.png")

        #get filename from DetermineTemperatureIcon
        temp_icon_svg = self.DetermineTemperatureIcon(weather['temperature'])
        temp_icon_path = Path(__file__).parent / "icons" / temp_icon_svg
        make_icon(str(temp_icon_path), color="#fffff0", size=(30, 30), output_path="app/ui/icons/thermometer.png")
        
        # Load the image and update the label
        new_icon = tk.PhotoImage(file=f"app/ui/icons/weather.png")
        self.weather_icon_label.config(image=new_icon)
        self.weather_icon = new_icon  # Keep a reference so Tk doesn't garbage-collect   
        self.temperature_icon = tk.PhotoImage(file=f"app/ui/icons/thermometer.png")
        self.temperature_icon_label.config(image=self.temperature_icon)


    def DetermineWeatherIcon(self, weather_code):
        if weather_code == 0:
            return "sun.svg"
        elif weather_code == 1:
            #return "partly_cloudy.png"
            return "cloud-sun.svg"
        elif weather_code == 2:
            #return "cloudy.png"
            return "cloudy.svg"
        elif weather_code == 3:
            #return "rain.png"
            return "cloud-rain-wind.svg"
        elif weather_code == 4:
            #return "thunderstorm.png"
            return "cloud-lightning.svg"
        elif weather_code == 5:
            #return "snow.png"
            return "snowflake.svg"
        return "cloudy.svg"
    
    def DetermineTemperatureIcon(self, temperature):
        if temperature < 35:
            return "thermometer-snow.svg"
        elif 35 <= temperature < 75:
            return "thermometer.svg"
        elif 75 <= temperature < 95:
            return "thermometer-sun.svg"
        elif 95 <= temperature:
            return "flame.svg"