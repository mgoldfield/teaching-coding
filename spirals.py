import turtle 
import random

def random_color():
	a = random.randint(0,255)
	b = random.randint(0,255)
	c = random.randint(0,255)
	return '#%02X%02X%02X' % (a,b,c)


def shape_spiral(sides, offset):
	angle = 360.0 / sides

	for i in range(0, 25):
		turtle.color(random_color())
		for i in range(0,sides):
			turtle.forward(200 / (sides - 2))
			turtle.right(angle + offset)


turtle.speed(0)
turtle.penup()
turtle.setposition(-200, 200)
turtle.pendown()

s = input("how many sides?")
o = input("offset?")

shape_spiral(int(s), int(o))

turtle.done()




