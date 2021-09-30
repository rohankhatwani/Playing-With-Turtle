import turtle

bob = turtle.Turtle()
bob.speed(30)
bob.getscreen().bgcolor("#994444")

bob.penup()
bob.goto((-200,100))
bob.pendown()

def star(bob,size):
	if size <= 10:
		return
	else:
		for i in range(5):
			bob.forward(size)
			star(turtle,size/3)
			bob.left(216)

star(bob,360)





turtle.done()