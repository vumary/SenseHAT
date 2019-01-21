#!/bin/python3

from sense_hat import *
from time import sleep
import random

sense = SenseHat()

#gyro

#colors
red = (255,0,0)
white = (255,255,255)

#type variables to represent up down left and right
left = 100
right = -100
x = 0
y = 0
dpitch = 0

sense.set_pixel(1, 1, white)

#while loops for the movement
while(True):
  gyro = sense.get_orientation()
  pitch = gyro["pitch"]
  print(pitch)
  if (pitch > 30.0 and x<7):
    x = x +1
    sense.clear()
    sense.set_pixel(x, y, red)
    sleep(0.01)
  if (pitch < 330.0 and x>0):
    x = x -1
    sense.clear()
    sense.set_pixel(x, y, red)
    sleep(0.01)
