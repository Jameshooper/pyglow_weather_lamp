import pywapi
import string
from PyGlow import PyGlow
from time import sleep
import urllib

pyglow = PyGlow() #Setup piglow and turn all off
pyglow.all(0)

yahoo_result = pywapi.get_weather_from_yahoo('FIXX0031') #get weather info from yahoo. Weather codes for city: https://www.edg3.uk/snippets/weather-location-codes/

condition = string.lower(yahoo_result['condition']['text']) #condition call. This gets a text readout of the current conditions
if condition in ["partly cloudy", "mostly cloudy", "cloudy"]: 
     pyglow.color("white", 150)

elif condition in ["mixed rain and snow" , "mixed snow and sleet" , "freezing drizzle" , "freezing rain" , "snow flurries" , "light snow showers" , "blowing snow" , "snow" , "hail" , "sleet" , "dust" , "heavy snow" , "scattered snow showers" , "snow showers" , "light snow", "light snow grains"]:
     pyglow.color("yellow", 150)	

elif condition in ["severe thunderstorms", "thunderstorms", "isolated thunderstorms" , "scattered thunderstorms" , "thundershowers"]:
     pyglow.color("red", brightness=150, speed=4000, pulse=True)

elif condition in ["mixed rain and sleet" , "drizzle" , "showers" , "scattered showers" , "mixed rain and hail"] :
     pyglow.color("blue", 150)
	
elif condition in ["windy" , "cold"]:
     pyglow.color("blue", 150)
     pyglow.color("red", 150)	

elif condition in ["clear" , "hot" , "sunny" , "fair"]:
     pyglow.color("green", 150)
	
elif condition in ["fog" , "foggy" , "haze" , "smokey" , "blustery"] : 
     pyglow.color("blue", 200)
     pyglow.color("white", 150)
 
else:
   pyglow.all(1)

		
				

		
