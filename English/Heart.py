from math import *
from turtle import *
from time import sleep
import platform


# X coordinate of the heart
def heart_x(k):
    return 20*sin(k)**3


# Y coordinate of the heart
def heart_y(k):
    return 12*cos(k) - 5*cos(2*k) - 2*cos(3*k) - cos(4*k)


# Turtle Settings                  #|—————————————————————————|#
title("Heart")                     #| Title of the window     |#
setup(width=1.0, height=1.0)       #| Fullscreen              |#
speed(0)                           #| Fastest drawing         |#
bgcolor("black")                   #| Background color        |#
color("red")                       #| Pen color               |#
pensize(5)                         #| Pen size                |#
tracer(10)                         #| Drawing speed           |#
scale = 20                         #| Scale of the heart      |#
                                   #|—————————————————————————|#


# Drawing the heart
for i in range(715):
    penup()
    goto(0, 0)
    pendown()
    goto(heart_x(i)*scale, heart_y(i)*scale)   # Draws the rays of the heart


# Reset the speed to default
tracer(0)

# First message
message1 = "I love you"
color("red")
penup()
goto(-220, 230)
for ch in message1:
    pendown()
    # Check the OS and set the font accordingly
    if platform.system() == "Windows":
        write(ch, align="center", font=("Lucida Handwriting", 55, "bold"))   # Windows
    elif platform.system() == "Darwin":
        write(ch, align="center", font=("Brush Script MT", 65, "bold"))      # macOS
    penup()                 #|————————————————————————————————|#
    forward(50)             #| Spacing between characters     |#
    update()                #| Update the screen              |#
    sleep(0.2)              #| Pause between characters       |#
                            #|————————————————————————————————|#

# Second message
message2 = "Andriana"
color("purple")
penup()
goto(-180, -50)
for ch in message2:
    pendown()
    write(ch, align="center", font=("Brush Script MT", 80, "bold"))
    penup()                 #|————————————————————————————————|#
    forward(50)             #| Spacing between characters     |#
    update()                #| Update the screen              |#
    sleep(0.3)              #| Pause between characters       |#
                            #|————————————————————————————————|#

# Clean up and end the drawing
                            #|——————————————————————————————————|#
hideturtle()                #| Hide the turtle                  |#
penup()                     #| Pull the pen up                  |#
goto(500, 500)              #| Move the turtle out of sight     |#
update()                    #| Update the screen                |#
done()                      #| Finish the turtle graphics       |#
                            #|——————————————————————————————————|#
