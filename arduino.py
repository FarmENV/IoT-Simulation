import requests
import random
import time
from datetime import datetime

''' Variables with the data the sensors should start '''
temp = 30.0
humidity = 80
food = 48
airQuality=(random.choice(["Good","Bad"]))
lastTemp = 30
lastAirQuality = "Good"

now = datetime.now()
date = now.strftime("%d/%m/%Y %H:%M:%S")

# The arduino ID, hardcoded in each installed system
arduinoId = "arduinoid1"

''' Request that runs when the system is turned on '''
REQUEST_URL = f"https://api-iot-farmenv.herokuapp.com/arduinoPost/?arduinoId={arduinoId}&date={date}"
_request = requests.get(REQUEST_URL)
print(_request.text)

''' This function checks if there is an important 
change in the sensors since the last measurement '''
def checkLast(temp, airQuality, lastTemp, lastAirQuality):

    if(airQuality!=lastAirQuality):
        return True
    elif((lastTemp-temp)>=1 or (temp-lastTemp)>=1):
        return True
    else:
        return False

''' Loop to run the sensors simulation every 3 seconds '''
while True:

    temp = round(random.uniform(temp-3, temp+3),2)
    if temp > 50:
        temp = 50
    elif temp < -15:
        temp = -15

    humidity = round(random.uniform(humidity-3, humidity+3),0)
    if humidity > 100:
        humidity = 100
    elif humidity < 0:
        humidity = 0
    
    food = random.randrange(food-5,food)
    if food < 0:
        food = 0

    airQuality=(random.choice(["Buena","Regular","Mala","¡Peligro!"]))
    
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")

    ''' If there is an important change in the sensors data
    it sends the data to the API '''
    if(checkLast(temp,airQuality, lastTemp, lastAirQuality)):
        """ The request for the data """
        REQUEST_URL = f"https://api-iot-farmenv.herokuapp.com/option/?arduinoId={arduinoId}&temp={temp}&food={food}&airQuality={airQuality}&date={date}&humidity={humidity}"
        _request = requests.get(REQUEST_URL)
        print(_request.text)

    # The variables for the last measurement are updated
    lastAirQuality = airQuality
    lastFood = food
    lastTemp = temp

    # Three seconds to start the next measurement
    time.sleep(3)
