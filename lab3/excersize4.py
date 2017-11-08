import turtle
turtle.speed(200)
turtle.pendown()
def lol():
	turtle.pendown()
	turtle.forward(150)
	turtle.right(64)
	turtle.forward(100)
	turtle.right(64)
	turtle.forward(40)
	turtle.penup()
	turtle.home()
	
for i in range (360):
	lol()
	turtle.right(i)
turtle.mainloop()

lol()



