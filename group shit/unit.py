from turtle import *
import math
import time
import random

ALIVE = True
class Unit(Turtle):
	def __init__(self, x, y):
		Turtle.__init__(self)
		self.x = x
		self.y = y
		self.ht()
		self.pu()
		self.shape("circle")


