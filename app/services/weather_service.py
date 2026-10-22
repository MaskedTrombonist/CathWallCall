import requests

class WeatherService:
    def __init__(self, lat= "47.679177", lon="-117.421667"):
        self.lat = lat
        self.lon = lon
        
    def fetch(self):
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": self.lat,
            "longitude": self.lon,
            "current_weather": True,
            "temperature_unit": "fahrenheit",
        }
        data = requests.get(url, params=params).json()
        w = data["current_weather"]
        return {
            "temperature": w["temperature"],
            "windspeed": w["windspeed"],
            "weathercode": w["weathercode"]
        }
    