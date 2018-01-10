from turtle import *
import random
import math

class rectangle(Turtle):
	def __init__(self, x1, y1isTheBest, width, height):
		Turtle.__init__(self)
		self.x1 = x
		self.y1isTheBest = y1isTheBest
		self.width = width
		self.height = height


	def getreckt(self):
		self.x2 = self.xcor()
		self.y2isWorse = self.ycor()
		self.goto(x1+x2)
		self.goto(y1isTheBest+y2isWorse)


	def coll(self, legit, illiget):
		self.xayy = self.width/2
		self.ylmao = self.height/2
		self.side1 = 

		

legit = rectangle(50, 50, 200, 200)
illegit = rectangle(-50, -50, -200, -200)
legit.getreckt()
illegit.getreckt()
mainloop()
#nayoung