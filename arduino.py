import requests
import random
import json

option = True
temp = 30
food = 3000

hash_password = "ECF389B6DDCF5D10D1D494924300A2ADC23AFAFD03FE9669C27774ED2895B6EC"

print("Wellcome")

while option:
    print("\nTemperature: ")
    temp = random.randrange(temp-2, temp+3)
    if temp > 45:
        temp = 45
    print(temp,"°C")

    print("\nFood: ")
    food = random.randrange(food-5,food)
    if food < 0:
        food = 0
    print(food,"g")

    print("\nAir Quality: ")
    airQuality=(random.choice(["Good","Bad"]))

    """ The request for the data """
    REQUEST_URL = f"http://127.0.0.1:5000/option/{hash_password}/?temp={temp}&food={food}&airQuality={airQuality}"
    _request = requests.get(REQUEST_URL)
    print(_request.text)


    """ Data obtained from the json """
    data = json.loads(_request.text)
    data_temp = data['temp']
    data_food = data['food']
    data_air = data['airQuality']
    print(data_temp)
    print(data_food)
    print(data_air)

    """ Close program """
    print("Do you want to stop the program? [Y/N]")
    _option = input()
    _option = _option.lower()

    if _option == 'y':
        option = False
