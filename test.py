#####
#
# PyGlow
#
#####
#
# Python module to control Pimoronis PiGlow
# [http://shop.pimoroni.com/products/piglow]
#
# * test.py - set brightness for each color individually
#
#####


from PyGlow import PyGlow


pyglow = PyGlow()

val = input("White: ")
pyglow.color("white", val)

val = input("Blue: ")
pyglow.color("blue", val)

val = input("Green: ")
pyglow.color("green", val)

val = input("Yellow: ")
pyglow.color("yellow", val)

val = input("Orange: ")
pyglow.color("orange", val)

val = input("Red: ")
pyglow.color("red", val)

val = input("All: ")
pyglow.all(val)
