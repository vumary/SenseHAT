from sense_hat import *
from time import sleep
from random import randint

sense = SenseHat()

sense.clear()
sleep(1)

while(True):
  x = randint(0,7)
  y = randint(0,7)
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  color = [r, g, b]
  sense.set_pixel(x, y, color)
  sleep(0.01)
