from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

# Creating the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game ")
screen.tracer(0)

# Creating two paddles right and left
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Creating a Ball
ball = Ball()

score = Score()

screen.listen()
screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with upper and lower walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.speed()
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.restart_position()
        score.l_score()

    if ball.xcor() < -380:
        ball.restart_position()
        score.r_score()

screen.exitonclick()
