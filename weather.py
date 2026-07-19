from exceptions import input_city
from config import weather_api_key
from storage import read, write
from logger import tracker
import requests


def search_weather():
    city = input_city()
    if not city:
        return
    
    api_key = weather_api_key()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            pressure = data['main']['pressure']
            weather_discription = data['weather'][0]['description']

            print(f"the weather of the {city} is .....")
            print(f"the tempreture is {temp} C: ")
            print(f"the temp feels like is {feels_like}C: ")
            print(f"the humidity is {humidity}: %")
            print(f"the wind speed is {wind_speed} m/s: ")
            print(f"the pressure is {pressure}hpa : ")
            print(f"the weather discription is {weather_discription}: ")

            try:
                history = read()
            except:
                history = {}

            history[city] = {
                'temp' : temp,
                'condition' : weather_discription
            }
            write(history)
            print("search history is saved and the weather condition is displyed! ")
            tracker.info(f"Search {city} is saved to database ")

        elif response.status_code == 404:
            print("invalid city name please check your spelling..")
            tracker.warning(f"the city name {city} is incorrect!")

    except Exception as error:
        print(f"No connection....{error}")
        tracker.error(f"cannot connect to the network {error}!")
    
    

def view_search_history():
    file = read()
    print(file)
    tracker.info("search history is displyed! ")
    
def clear_history():
    write({})
    print("clear search history ")
    tracker.info("Clear all search history!")

