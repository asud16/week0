# Flower excercise (4.2) from Week 0

# Name: Aparna Sud


from TurtleWorld import *   	
world = TurtleWorld()			
bob = Turtle()				

from bss_polygon import *

def petal(Turtle, r, angle):
	for i in range(2):
		arc(Turtle, r, angle)
		lt(Turtle, 180-angle) #how does this function work?

def flower(Turtle, n, r, angle):
	petal(Turtle, r, angle)
	lt(Turtle, 360.0/n)

petal(bob, 8, 45) # not drawing
