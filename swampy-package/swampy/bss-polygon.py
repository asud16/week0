# Polygon excercise from Week 0

# Name: Aparna Sud


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()		

import math		

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

def circle(Turtle, r):
	circum = 2 * math.pi * r
	n = 100
	distance = circum / n
	polygon(Turtle, distance, n)

#circle(bob, 5)
#Refactoring portion: 

def polyline(Turtle, distance, n, angle): 
	for i in range(n):
		fd(Turtle, distance)
		lt(Turtle, angle)

def polygon2(Turtle, distance, n):
	angle = 360.0/n
	polyline(Turtle, distance, n, angle)

def arc(Turtle, r, angle):
	arc_distance = 2 * math.pi * r * angle/360
	n = int(arc_distance/3) + 1 # why do this?
	step_distance = arc_distance/n
	step_angle = float(angle)/n
	polyline(Turtle, step_distance, n, step_angle)

def circle2(Turtle, r):
	arc(Turtle, r, 360)

circle2(bob, 10)

wait_for_user()					
