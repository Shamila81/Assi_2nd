#Task 01
import requests

response = requests.get('https://api.chucknorris.io/jokes/random')

if response.status_code == 200:

    joke_data = response.json()
    joke_text = joke_data['value']
    print(joke_text)
else:
    print('Error fetching joke: ' + str(response.status_code))

#Task 02

import requests
import json

api_key = "YOUR_API_KEY"

municipality = input("Enter municipality name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={api_key}"

response = requests.get(url)

if response.status_code == 200:

    data = json.loads(response.text)

    weather_condition = data['weather'][0]['description']
    temperature = data['main']['temp'] - 273.15

    print(f"Weather in {municipality}: {weather_condition}")
    print(f"Temperature in Celsius: {temperature:.2f}°C")
else:
    print(f"Error retrieving weather information for {municipality}.")

