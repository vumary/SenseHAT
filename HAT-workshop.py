from sense_hat import *
from time import sleep
from random import randint



sense = SenseHat()

#player: brown
#walls: blue
#ground: white
#end: green
#colors
b = [33,167, 255]#[33, 166, ]255
brownboi = [255,0,0]#[196, 158, 106]
w = [0,0,0]
g = [0, 255, 0]

map =[
w,w,w,w,w,w,w,w,
b,b,b,b,w,b,b,b,
w,w,w,w,w,w,w,w,
b,b,b,w,b,w,w,w,
w,w,b,w,b,b,b,b,
w,w,w,w,w,w,w,w,
w,w,b,w,b,w,b,w,
b,b,b,b,b,g,b,b
]


#type variables to represent up down left and right
left = 100
right = -100
x = 0
y = 0

sense.set_pixels(map)


def won():
  return (sense.get_pixel(x,y)==[g[0],g[1]-3,g[2]])
    
#while loops for the movement
while(True):
  
  print("actual: %s" %sense.get_pixel(5, 7))
  print("equal to? %s" %[g[0],g[1]-3,g[2]])

  gyro = sense.get_orientation()
  pitch = gyro["pitch"]
  roll = gyro["roll"]
  
  #up
  if (roll < 350 and roll > 180 and y>0 and not(sense.get_pixel(x,y-1)==[b[0]-1,b[1]-3,b[2]-7])):
    sense.set_pixel(x,y,w)
    y -= 1;
    sense.set_pixel(x, y, brownboi)
    sleep(0.01)
  #down
  if (roll > 10 and roll < 180 and y<7 and not(sense.get_pixel(x,y+1)==[b[0]-1,b[1]-3,b[2]-7])):
    sense.set_pixel(x,y,w)
    y += 1;
    sense.set_pixel(x, y, brownboi)
    sleep(0.01)
  #left
  if (pitch > 10 and pitch < 180 and x>0 and not(sense.get_pixel(x-1,y)==[b[0]-1,b[1]-3,b[2]-7])):
    sense.set_pixel(x,y,w)
    x -= 1
    sense.set_pixel(x, y, brownboi)
    sleep(0.01)
  #right
  if (pitch < 350 and pitch > 180 and x<7 and not(sense.get_pixel(x+1,y)==[b[0]-1,b[1]-3,b[2]-7])):
    sense.set_pixel(x,y,w)
    x += 1
    sense.set_pixel(x, y, brownboi)
    sleep(0.01)
  if(x==5 and y==7):
    sense.show_message("good game")
    break
