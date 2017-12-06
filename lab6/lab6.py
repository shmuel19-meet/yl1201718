from turtle import *
import random
import math

colormode(255)

class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)

ball1 = Ball(70,"red", 5)
ball2 = Ball(80, "blue", 5)
ball1.goto(5, 100)
ball2.goto(5, 10)

def collision_check(ball1, ball2):
	r1 = ball1.radius
	r2 = ball2.radius
	x1 = ball1.xcor()
	x2 = ball2.xcor()
	y1 = ball1.ycor()
	y2 = ball2.ycor()
	d = pow((x2-x1),2) + pow((y2-y1), 2)
	d = sqrt(d)
	print(d)
	ultR = ball1.radius+ball2.radius
	print(ultR)
	if ultR >= d:
		print("collision!")
collision_check(ball1, ball2)
mainloop()