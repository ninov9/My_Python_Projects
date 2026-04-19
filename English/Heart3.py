import math
import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)
t.speed(0)
turtle.bgcolor("black")
t.color("red")

def heart1(k):
    return 15 * math.sin(k) ** 3

def heart2(k):
    return 12 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k)

t.penup()
for i in range(750):
    t.goto(heart1(i)*18, heart2(i)*18)
    t.pendown()

t.penup()
t.goto(115, 0)
t.pendown()
t.write("I LOVE YOU", False, "right", ("arial", 30, "bold"))
t.penup()
t.goto(0, -60)
t.pendown()
t.write("Andriana", False, "center", ("arial", 30, "bold"))


t.hideturtle()
turtle.done()