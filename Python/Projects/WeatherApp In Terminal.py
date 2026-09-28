import requests

api = 'b155432dc7efa6fec38f66a561c58626'
user_input = input('Enter your city: ')

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}"
                            f"&units=imperial&APPID={api}")
if weather_data.json()['cod'] == '404':
    print("Sorry, we couldn't find that city.")
else:
    weather = weather_data.json()['weather'][0]['main']
    temperature = weather_data.json()['main']['temp']
    C = (temperature - 32) / (9 / 5)
    print(f'Weather In {user_input} is: \n{weather}')
    print(f'Temperature is: \n{temperature} Fahrenheit\n{C: .2f} Celsius')