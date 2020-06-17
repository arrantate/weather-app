import requests
import json
import wikipedia

class Weather_API():
    def __init__(self, city):
        api_key = "b42f54e6e9d72bb93bf01757428e2325"
        full_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(full_url)
        response = response.json()
        self.cod = response['cod']

        if self.cod != '404':     
                   
            self.city = response['name']
            self.country = response['sys']['country']
            self.weather = response['main']

            description = response['weather'][0]['description']
            self.description = description[0].upper() + description[1:]

            self.temp = round((response['main']['temp'] - 273.15), 1)
            self.temp_min = round((response['main']['temp_min'] - 273.15), 1)
            self.temp_max = round((response['main']['temp_max'] - 273.15), 1)
            self.pressure = response['main']['pressure']
            self.humidity = response['main']['humidity']

    # def __str__(self):
    #     return f"The weather in {self.city}, {self.country} is {self.description}"

class Wiki_API():
    def __init__(self, city):
        wiki = wikipedia.page(city)
        self.url = wiki.url
        self.content = wiki.content
        self.summary = wikipedia.summary(city, sentences=3)


