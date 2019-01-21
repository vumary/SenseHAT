from sense_hat import *
from time import sleep
from random import randint

sense = SenseHat()

#colors
red = (255,0,0)
white = (255,255,255)
blue = (0, 0, 255)
_blue = (30, 30, 200)

#type variables to represent up down left and right
left = 100
right = -100
x = 0
y = 0
dpitch = 0

#while loops for the movement
while(True):
  gyro = sense.get_orientation()
  pitch = gyro["pitch"]
  roll = gyro["roll"]
  print("pitch: %s"  %pitch)
  print("roll: %s" %roll)
  if (pitch > 10 and pitch < 180 and x>0):
    #can't make trail bc sense.clear()
    sense.set_pixel(x, y, _blue)
    x -= 1
    sense.clear()
    sense.set_pixel(x, y, blue)
    sleep(0.01)
  if (pitch < 350 and pitch > 180 and x<7):
    x += 1
    sense.clear()
    sense.set_pixel(x, y, blue)
    sleep(0.01)
  if (roll > 10 and roll < 180 and y<7):
    y += 1;
    sense.clear()
    sense.set_pixel(x, y, blue)
    sleep(0.01)
  if (roll < 350 and roll > 180 and y>0):
    y -= 1;
    sense.clear()
    sense.set_pixel(x, y, blue)
    sleep(0.01)


'''
while True:
    x = randint(0, 7)
    y = randint(0, 7)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    sense.set_pixel(x, y, r, g, b)
    sleep(0.01)
'''

'''

sense.low_light = True

X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White
Y = [0, 0, 0] #off

heart = [
Y, X, X, Y, Y, X, X, Y,
X, X, X, X, X, X, O, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
Y, X, X, X, X, X, X, Y,
Y, Y, X, X, X, X, Y, Y,
Y, Y, Y, X, X, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
]

sense.set_pixels(heart)
'''
#sense.show_message("hello")

#fahren = (sense.get_temperature()*(9/5))+32
#cel = sense.get_temperature()
#sense.show_message("Temperature: %s C" % cel)
