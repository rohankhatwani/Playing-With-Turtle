import turtle
import math

bob = turtle.Turtle()
bob.color("red","yellow")
bob.speed(10)

for i in range(2000):
	bob.forward(10)
	bob.left(math.sin(i/10)*25)
	bob.left(20)