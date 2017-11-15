class Animal (object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound 
		self.name = name
		self.age = age
		self.favorite_color = favorite_color

	def eat(self,food):
		print("yummy"+self.name+"is eating"+food)

	def description(self):
		print(doggo.name + "is " + self.age + "years old and loves the color " + self.favorite_color)
	def makesound(self):
		print((self.sound+"")*3)

doggo = Animal("woof","doggo",18,"Red")

doggo.makesound()
class Person (object):
	def __init__(self,age,city,gender,ffood,fbreakfast):
		self.age = age
		self.city = city
		self.gender = gender
		self.ffood = ffood
		self.fbreakfast = fbreakfast
	def eatbreakfast(self):
		print(self.fbreakfast)
	def eatffood(self):
		print(self.ffood)
Gary = Person(35, "London", "attack hellicopter", "Hamburger","cereal")
Gary.eatbreakfast()
Gary.eatffood()
class Song (object):
	def __init__(self, lyrics,line2, line3):
		self.lyrics = lyrics
		self.line2 = line2
		self.lin3 = line3
Ting = Song("the ting goes skrra pa pa ka ka ka", "skibbidy ka ka and a pum pum purru boom")
	def sing_me_a_song(self):
		for i in self.lyrics
