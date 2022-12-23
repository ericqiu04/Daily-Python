import turtle as t
import random
screen = t.Screen()
screen.setup(width = 500, height = 500)

def movement():
    return random.randint(1,10)

bet = screen.textinput(title = "make your bet", prompt = "Which turtle do you think will win? Enter a colour: ")
print(bet)


#creating turtles
red = t.Turtle()
red.color("red")
red.shape("turtle")

blue = t.Turtle()
blue.color("blue")
blue.shape("turtle")

green = t.Turtle()
green.color("green")
green.shape("turtle")

yellow = t.Turtle()
yellow.color("yellow")
yellow.shape("turtle")

orange = t.Turtle()
orange.color("orange")
orange.shape("turtle")

purple = t.Turtle()
purple.color("purple")
purple.shape("turtle")


#go to positions
red.penup()
red.goto(-230, 150)
blue.penup()
blue.goto(-230, 100)
green.penup()
green.goto(-230, 50)
yellow.penup()
yellow.goto(-230,-50)
orange.penup()
orange.goto(-230,-100)
purple.penup()
purple.goto(-230,-150)
all_turtles = [red, blue, green, yellow, orange, purple]
print(screen.window_width()/2)

while red.xcor() <= screen.window_width()/2 or blue.xcor() <= screen.window_width()/2 or green.xcor() <= screen.window_width()/2 or yellow.xcor() <= screen.window_width()/2 or orange.xcor() <= screen.window_width()/2 or purple.xcor() <= screen.window_width()/2:
    red.forward(movement())
    print(red.xcor())
    blue.forward(movement())
    green.forward(movement())
    yellow.forward(movement())
    orange.forward(movement())
    purple.forward(movement())

for turtle in all_turtles:
    if(turtle.xcor() > screen.window_width()/2):
        winner = turtle.pencolor()

if(winner == bet):
    print("You won!")
else:
    print(f"You lost! The winner was {winner}")





