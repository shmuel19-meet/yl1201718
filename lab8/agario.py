import turtle
import time
import random
import math
from ball import Ball
turtle.tracer(0)
turtle.colormode(255)
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5
BALLS = []
#-----------------------
MY_BALL = Ball(0,0,5,5, 50)
for i in range(NUMBER_OF_BALLS):
	x = random.randint(-SCREEN_WIDTH+MINIMUM_BALL_RADIUS, SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT-MINIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(), random.random())
	NEW_BALL = Ball(x,y,dx,dy,radius)
	BALLS.append(NEW_BALL)

def move_all_balls():
	for i in BALLS:
		i.move(SCREEN_WIDTH, SCREEN_HEIGHT)

def collide(ball_a, ball_b):
	if (ball_a == ball_b):
		return False
	temp_a_x = ball_a.xcor()
	temp_a_y = ball_a.ycor()
	temp_b_x = ball_b.xcor()
	temp_b_y = ball_b.ycor()
	distance = math.sqrt(math.pow(temp_b_x - temp_a_x, 2)+math.pow(temp_b_y - temp_a_y, 2))+10
	radiusum = ball_a.r + ball_b.r
	if (distance <= radiusum):
		print("cllision")
		return True
	else:
		return False
def check_all_balls_collisions():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a, ball_b):

				ball_a_radius = ball_a.r
				ball_b_radius = ball_b.r
				rand_x_cor = random.randint(-SCREEN_WIDTH, SCREEN_WIDTH)
				rand_y_cor = random.randint(-SCREEN_HEIGHT, SCREEN_HEIGHT)
				rand_dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				rand_dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				rand_radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				rand_r = random.randint(0, 255)
				rand_g = random.randint(0, 255)
				rand_b = random.randint(0, 255)
				rand_color = (rand_r, rand_g, rand_b)

				if ball_a_radius>ball_b_radius:

					ball_b.goto(rand_x_cor, rand_y_cor)
					ball_b.dx = rand_dx
					ball_b.dy = rand_dy
					ball_b.r = rand_radius
					ball_b.shapesize(ball_b.r/10)
					ball_b.color = (rand_r, rand_g, rand_b)
					ball_a.r+=1
					ball_a.shapesize(ball_a.r/10)
				if ball_a_radius == ball_b_radius:
					pass
				else:
					ball_a.goto(rand_x_cor, rand_y_cor)
					ball_a.dx = rand_dx
					ball_a.dy = rand_dy
					ball_a.r = rand_radius
					ball_a.shapesize(ball_a.r/10)
					ball_a.color = (rand_r, rand_g, rand_b)
					ball_b.r+=1
					ball_b.shapesize(ball_b.r/10)


def check_myball_collision():
	for i in BALLS:
		if collide(MY_BALL, i):
			rand_x_cor = random.randint(-SCREEN_WIDTH, SCREEN_WIDTH)
			rand_y_cor = random.randint(-SCREEN_HEIGHT, SCREEN_HEIGHT)
			rand_dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
			rand_dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
			rand_r = random.randint(0, 255)
			rand_g = random.randint(0, 255)
			rand_b = random.randint(0, 255)
			rand_color = (rand_r, rand_g, rand_b)
			rand_radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
			temp_radius = i.r
			MY_BALL_radius = MY_BALL.r
			if(temp_radius>=MY_BALL_radius):
				
				return False

			i.goto(rand_x_cor, rand_y_cor)
			i.dx = rand_dx
			i.dy = rand_dy
			i.r = rand_radius
			i.color = (rand_r, rand_g, rand_b)

			MY_BALL.r+=5
			MY_BALL.shapesize(MY_BALL.r/10)

	return True
def movearound(event):
	MY_BALL.goto(event.x-SCREEN_WIDTH, SCREEN_HEIGHT-event.y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()
while RUNNING == True:
	if SCREEN_WIDTH != turtle.getcanvas().winfo_width()/2:
		SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
	if SCREEN_HEIGHT != turtle.getcanvas().winfo_height()/2:
		SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

	move_all_balls()
	check_all_balls_collisions()
	check_myball_collision()

	turtle.update()
	time.sleep(SLEEP)

turtle.ht()
turtle.mainloop()