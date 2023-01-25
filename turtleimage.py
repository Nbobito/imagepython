import sys
from time import sleep
from PIL import Image
import numpy
import textwrap
from turtle import Turtle, Screen, tracer, update
import threading


file_name = "car.jpeg"
image = ""


try:
    image = Image.open(file_name)
except:
    print ("File not found.")
    sys.exit()

size = image.size
ratio = size[1] / size[0]
detail = 150
resized_image = image.resize((detail, int(detail * ratio)))
loaded_image = resized_image.load()
width, height = resized_image.size

class AdvancedTurtle(Turtle):
    
    def __init__(self, frame_rate: int=15):
        super().__init__()
        self.frame_rate = frame_rate
        tracer(0,0)
    
    
    
main = Screen()
main.colormode(255)

a = AdvancedTurtle(1)


top_left = (int(-0.5*main.window_width()),int(0.5*main.window_height()))

print(top_left)
a.penup()
a.goto(top_left)


pixel_size = 6
a.pensize(pixel_size)
for y in range(height):
    for x in range(width):
        a.pendown()
        red, green, blue = loaded_image[x, y]
        a.color((red, green, blue))
        a.forward(pixel_size)
    a.penup()
    a.right(90)
    a.forward(pixel_size)
    a.left(90)
    x, y = a.pos()
    a.goto(top_left[0], y)
    update()
    

update()
main.exitonclick()

