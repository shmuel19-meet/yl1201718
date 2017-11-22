
from turtle import *
import random
colormode(255)
class Square(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape("square")

	def random(self):
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color(r, g, b)

square1 = Square(5)
square1.random()
#square1.random((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
begin_poly()
for i in range(6):
	pendown()
	forward(20)
	right(60)
end_poly()
register_shape(get_poly())

class Hexagon(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape("hexagon")

mainloop()