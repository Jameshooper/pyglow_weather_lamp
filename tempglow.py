import pywapi
import string
from PyGlow import PyGlow
from time import sleep
import urllib

pyglow = PyGlow() #Setup piglow and turn all off
pyglow.all(0)


yahoo_result = pywapi.get_weather_from_yahoo('FIXX0031') #This gets the weather from Yahoo. Set the code for your city: https://www.edg3.uk/snippets/weather-location-codes/
temp = yahoo_result['condition']['temp'] # This gets only the temperature from the conditions
print temp
temperature=int(temp)
if temperature <-20:
   pyglow.color("blue", 255)
elif temperature < -10:
     pyglow.color("blue", 255)
     pyglow.color("green", 225)
elif temperature < -5:
     pyglow.color("blue", 180)
     pyglow.color("green", 255)
elif temperature < 0:
     pyglow.color("green", 255)
elif temperature < 5:
     pyglow.color("green", 255)
     pyglow.color("yellow", 200)
     pyglow.color("orange", 210)
     pyglow.color("red", 200)
elif temperature < 10:
     pyglow.color("green", 240)
     pyglow.color("yellow", 200)
     pyglow.color("orange", 255)
     pyglow.color("red", 220)
elif temerature < 15:
     pyglow.color("green", 220)
     pyglow.color("yellow", 255)
     pyglow.color("orange", 255)
     pyglow.color("red", 255)
elif temperature < 20:
     pyglow.colur("green", 180)
     pyglow.color("yellow", 255)
     pyglow.color("orange", 255)
     pyglow.color("red", 255)
elif temperature < 25:
     pyglow.color("green", 90)
     pyglow.color("yellow", 255)
     pyglow.color("orange", 255)
     pyglow.color("red", 255)
elif temperature < 30:
     pyglow.color("red", 255)
     pyglow.color("orange", 255)
elif temperature < 40:
     pyglow.color("red", 255)
     pyglow.color("blue", 180)
     pyglow.color("orange", 255)
     pyglow.color("red", 255) 
else: pyglow.all(255)

	
