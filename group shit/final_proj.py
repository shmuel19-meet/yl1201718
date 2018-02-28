from turtle import *
import turtle
import math
import time
import random
from unit import Unit

turtle.ht()
turtle.bgcolor("black")
turtle.color("yellow")
turtle.write ("achtung" ,align = "center" , font = ("ariel" ,100 , "normal"))
turtle.color("red")
turtle.pensize(10)

#---------------------------------------------
SNAKEZ = []
ALIVE = True
#to finish-----------------------------------|

snake = turtle.clone()
SNAKEZ.append(snake)
UP = 0
LEFT = 2
RIGHT = 3
direction = UP

def left():
	global direction
	direction = LEFT

def right():
	global direction
	direction = RIGHT

#################moving	
def move_left(event):
	snake.left(25)
getcanvas().bind("<Left>", move_left)
listen()

def move_right(event):
	snake.right(25)
getcanvas().bind("<Right>", move_right)
listen()

while(direction == LEFT):
	snake.left(25)
while(direction == RIGHT):
	snake.right(25)
#########################

while(ALIVE == True):
	new_unit = Unit(snake.xcor()-1,snake.ycor()-1)
	snake.forward(1)
	SNAKEZ.append(new_unit)



mainloop()