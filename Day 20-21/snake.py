import turtle as t

screen = t.Screen()
screen.setup(width = 1000, height = 1000)
screen.bgcolor("black")
screen.title("Snake Game")



starting_positions = [(-20,0), (0,0), (20,0)]

segments = []
for position in starting_positions:
    new_segment = t.Turtle()
    new_segment.shape("square")
    new_segment.color("light green")
    new_segment.penup()
    new_segment.setpos(position)
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    for s in segments:
        s.forward(10)

screen.exitonclick()