from turtle import *
import math
import random
import time
colormode(255)
tracer(0)

class Ball(Turtle):
	def __init__(self, x, y, dx, dy, r, color):
		Turtle.__init__(self)
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.r = r
		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)
		self.color(r, g, b)
		self.shape("circle")

	def move(self, screen_width, screen_height):
		current_x = self.xcor()
		current_x = self.xcor()
		new_x = current_x+self.dx
		current_y = self.ycor()
		new_y = current_y+dy
		right_side_ball = new_x+self.r
		left_side_ball = new_x-self.r
		up_side_ball = new_y+self.r
		down_side_ball = new_y-self.r
		self.goto(new_x, new_y)

		if(right_side_ball >= screen_width):
			self.dx = -self.dx

		if(left_side_ball <= (-screen_width)):
			self.dx = -self.dx

		if(up_side_ball >= screen_height):
			self.dy = -self.dy

		if(down_side_ball <= -screen_height):
			self.dy = -self.dy