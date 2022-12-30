import turtle as t
import time
from snake import Snake
from food import Food

score = 0
screen = t.Screen()
screen.setup(width = 1000, height = 1000)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.update()
game_is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #see if touching
    if snake.head.distance(food) < 20:
        food.hideturtle()
        score +=1
        del food
        print("nom nom")
        food = Food()




screen.exitonclick()