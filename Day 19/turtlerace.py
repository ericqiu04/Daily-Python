import turtle as t

screen = t.Screen()
screen.setup(width = 500, height = 500)

bet = screen.textinput(title = "make your bet", prompt = "Which turtle do you think will win? Enter a colour: ")
print(bet)

screen.exitonclick()

