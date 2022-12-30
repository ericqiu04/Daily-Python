import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#creating objects
snake = Snake()
food = Food()
score = Scoreboard()

#screen
screen = t.Screen()
screen.setup(width = 1000, height = 1000)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


#score
score.color("white")
score.penup()
score.goto(0, 450)
score.hideturtle()


screen.update()
game_is_on = True

#movement listener
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

#game
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score.penup()
    #see if touching
    if snake.head.distance(food) < 20:
        food.hideturtle()
        score.addScore()
        del food
        print("nom nom")
        food = Food()
        score.clear()
        screen.title(score.getScore())
        snake.extend()

    #collision with tail
    for s in snake.segments[1:]:
        if snake.head.distance(s) < 10:
            game_is_on = False
            score.gameOver()
    #collision with walls
    if snake.head.xcor() >480 or snake.head.xcor() < -480 or snake.head.ycor() >480 or snake.head.ycor() < -480:
        game_is_on = False
        score.gameOver()





screen.exitonclick()