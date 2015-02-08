from PyGlow import PyGlow
from time import sleep
import os
pyglow = PyGlow()
pyglow.all(0)


for x in range(0, 15):
   pyglow.color("green", brightness=255, speed=500, pulse=True)
   sleep(1)

os.system("sudo python /home/pi/pyglow/tempglow.py")
#os.system("sudo python /home/pi/pyglow/weatherpyglow.py")    #Set either of these, depending on which type of pyglow lamp you want to reset to

