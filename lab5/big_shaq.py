begin_poly()
for i in range(6):
	pendown()
	forward(20)
	right(60)
end_poly()

register_shape("my_hex",get_poly())

class Hexagon(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape("my_hex")
hexa = Hexagon(2)
