from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import random
from text import Text

LIST_COLOR = ["red", "yellow", "green", "blue", "purple"]
COLOR = random.choice(LIST_COLOR)

text = Text()
screen = Screen()
screen.setup(width= 600, height=600)
screen.bgcolor("black")
screen.title("Snaky Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()
score_board.write("")



screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #collision with food
    if snake.head.distance(food) < 25:
        food.refresh()
        snake.extend()
        score_board.increase_score()


    #detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # game_is_on = False
        # score_board.game_over()
        score_board.reset()
        snake.reset()


    #snake collided with its tail
        #trigger gameover
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # score_board.game_over()
            score_board.reset()
            snake.reset()
screen.exitonclick()