# Polygon excercise from Week 0

# Name: Aparna Sud


from TurtleWorld import *   	
world = TurtleWorld()			
bob = Turtle()				

def square(Turtle, distance):
	for i in range(4):
		fd(Turtle, distance)
		lt(Turtle)

# square(bob, 100)

def polygon(Turtle, distance, n):
	angle = 360/n
	for i in range(n):
		fd(Turtle, distance)
		lt(Turtle, angle)

#polygon(bob, 100, 5)

def circle(Turtle, radius):
	circum = 2 * math.pi * radius
	n = 100
	distance = circum / n
	polygon(Turtle, distance, n)

#circle(bob, 50)
#not drawing the circle on the program

def arc(Turtle, radius, theta):
	theta = angle
	circle(Turtle, distance, n)

arc(bob, 50, 30)
#not sure how to do this function

wait_for_user()					
