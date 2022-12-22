import turtle as t

sketch = t.Turtle()

def forward():
    sketch.forward(10)

def backward():
    sketch.backward(10)

def rotate():
    sketch.left(5)

def crotate():
    sketch.right(5)

def clear():
    sketch.hideturtle()
    sketch.penup()
    sketch.goto(0,0)
    sketch.clear()
    sketch.pendown()
    sketch.showturtle()


screen = t.Screen()
screen.listen()
screen.onkey(key = "w", fun = forward)
screen.listen()
screen.onkey(key = "s", fun = backward)
screen.listen()
screen.onkey(key = "d", fun = rotate)
screen.listen()
screen.onkey(key = "a", fun = crotate)
screen.onkey(key = "space", fun = clear)

screen.exitonclick()
