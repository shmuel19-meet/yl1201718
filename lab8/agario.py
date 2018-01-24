import turtle
import time
import random
from ball import Ball
#turtle.tracer(0)
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

def Balls_iteration(BALLS):
	for i in BALLS:
		NEW_BALL.move(SCREEN_WIDTH, SCREEN_HEIGHT)

def collide(ball_a, ball_b):
	if (ball_a == ball_b):
		return False
	temp_a_x = ball_a.xcor()
	temp_a_y = ball_a.ycor()
	temp_b_x = ball_b.xcor()
	temp_b_y = ball_b.ycor()
	distance = sqrt(pow(temp_b_x - temp_a_x)+pow(temp_b_y - temp_a_y))+10
	radiusum = ball_a.r + ball_b.r
	if (distance <= radiusum):
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
				rand_radius = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				rand_r = random.randint(0, 255)
				rand_g = random.randint(0, 255)
				rand_b = random.randint(0, 255)
				rand_color = colormode(r, g, b)

				if ball_a_radius>ball_b_radius:

					ball_b.goto(rand_x_cor, rand_y_cor)
					ball_b.dx = rand_dx
					ball_b.dy = rand_dy
					ball_b.r = and_radius
					ball_b.color(r, g, b)
					ball_a.r++
					ball_a.shapesize++

				else:
					ball_a.goto(rand_x_cor, rand_y_cor)
					ball_a.dx = rand_dx
					ball_a.dy = rand_dy
					ball_a.r = and_radius
					ball_a.color(r, g, b)
					ball_b.r++
					ball_b.shapesize++

def check_myball_collision:
	for i in BALLS:
		if collide(my_ball, i)
		temp_radius = i.r
		my_ball_radius = my_ball.r


turtle.ht()
turtle.mainloop()