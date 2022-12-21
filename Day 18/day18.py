
import turtle as t
from turtle import Screen as s
import random

#turtle
tim = t.Turtle()

#screen
screen = s()

#screen dimensions
sw = screen.window_width()
sh = screen.window_height()

#color
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

def printDot():
    for i in range(int(sw / 50 - 1)):
        tim.color(random_color())
        tim.dot(20)
        tim.penup()
        tim.forward(50)
        tim.pendown()

def run():
    width = 50 - screen.window_width() / 2
    height = 40 - screen.window_height() / 2
    for i in range(int(sh / 50 )):
        tim.hideturtle()
        tim.penup()
        tim.goto(width, height)
        tim.showturtle()
        tim.pendown()
        printDot()
        height += 50


#start
run()

screen.exitonclick()