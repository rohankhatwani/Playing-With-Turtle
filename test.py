#Turtle graphics library - fun animations
import turtle

bob = turtle.Turtle()
# bob.forward(100)
# bob.left(45)
# bob.forward(100)
# bob.right(90)
# bob.forward(100)

bob.color("red","cyan")

bob.begin_fill()
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)

bob.penup()
bob.forward(150)
bob.pendown()
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.end_fill()


turtle.done()
# This keeps animation window open to see what we have done