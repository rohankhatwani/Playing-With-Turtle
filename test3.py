import turtle
import math

bob = turtle.Turtle()
bob.color("red","yellow")
bob.speed(10)

for i in range(2000):
	bob.forward(math.sqrt(i))
	bob.left(i%180)