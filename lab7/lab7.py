from turtle import *
import random
import math

class rectangle(Turtle):
	def __init__(self, x1, y1isTheBest, x2, y2isWorse):
		Turtle.__init__(self)
		self.width = math.fabs(x1 - x2)
		self.height = math.fabs(y1isTheBest-y2isWorse)

		self.x1 = x1
		self.x2 = x2
		self.y1isTheBest = y1isTheBest
		self.y2isWorse = y2isWorse

	def getreckt(self):
		for i in range(2):

			self.forward(self.width)
			self.left(90)
			self.forward(self.height)
			self.left(90)

	def coll(self, legit, illiget):
		xd = sqrt(pow((x1-x2),2))
		yd = sqrt(pow((self.y1isTheBest-self.y2isWorse),2))
		xc = self.width/2
		yc = self.height/2
		cc = self.width+self.height
		if(xd >= legit.)

legit = rectangle(50, 50, 200, 200)
legit.getreckt()

mainloop()