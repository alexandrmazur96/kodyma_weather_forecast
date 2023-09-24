import requests
import json
import sys

class WeatherApiClient:
    BASE_URL = "https://api.weatherapi.com/v1"
    FORECAST_URI = "/forecast.json"
    LANGUAGE = "uk" # Ukrainian language
    KODYMA_LAT = 48.0933357 # latitude
    KODYMA_LNG = 29.1044082 # longitude

    def __init__(self, apiKey):
        self.apiKey = apiKey

    def todayWeather(self):
        requestUrl = self.BASE_URL + self.FORECAST_URI + "?key=" + self.apiKey + "&q=" + str(self.KODYMA_LAT) + "," + str(self.KODYMA_LNG) + "&lang=" + self.LANGUAGE + "&aqi=yes&alerts=yes&days=1"
        response = requests.get(requestUrl)
        if response.status_code != 200:
            sys.stderr.write("Unable to obtain weather. Status Code: " + str(response.status_code) + "; Details: " + str(response.content))
            exit(1)
        return json.loads(response.content)