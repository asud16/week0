# Hello excercise from Week 0

# Name: Aparna Sud 

from TurtleWorld import *   	
world = TurtleWorld()			
bob = Turtle()				

# H 
lt(bob)
fd(bob, 100)
bk(bob, 50)
rt(bob)
fd(bob,50)
lt(bob)
fd(bob, 50)
bk(bob, 100)
pu(bob)
fd(bob,100)
pd(bob)

#E 
for i in range(2): 
	rt(bob)
	fd(bob,50)
	bk(bob,50)
	lt(bob)
	bk(bob,50)

#LL

rt(bob)

for i in range(2):
	fd(bob,100)
	bk(bob,50)
	lt(bob)
	fd(bob,100)
	bk(bob,100)
	rt(bob)

#0
pu(bob)
fd(bob,50)
pd(bob)

for i in range(4):
	fd(bob,100)
	lt(bob)

wait_for_user()					
