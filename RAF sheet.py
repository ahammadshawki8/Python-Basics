import math
import turtle
import random

a=turtle.Turtle()
a.speed(999999999999999999999999999999999999)

a.penup()
a.goto((-400,0))
a.pendown()

a.getscreen().bgcolor("black")
a.color("red")

for  i in range(850):
    a.forward(300)
    a.left(i*math.pi)
    a.right(45)
    a.goto((random.randint(-600,600),(random.randint(-300,300))))

turtle.done()
