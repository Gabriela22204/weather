import requests
import json
from dotenv import dotenv_values

BASE_URL = "http://api.weatherstack.com/"
CITY = "New York"

envVariables = dotenv_values()

url = BASE_URL + "current?access_key=" + envVariables['API_KEY'] + "&query=" + CITY


try:
    response = requests.get(url).json()
    json_data = json.dumps(response, indent=4)   
    try:
        with open("weather_data.json", "w") as data:
            data.write(json_data)
            
            print(json_data)            
    except:
        print('Failure to write json in file')
except:
    print('Your API request failed. Please try again.')
    
