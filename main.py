from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")

screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")

game_running = True
while game_running:
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # detect collision with left paddle
    if ball.xcor() < -330 and ball.distance(paddle_left) < 50:
        ball.bounce_x()

    # detect collision with left wall
    if ball.xcor() < -390:
        scoreboard.right_score += 1
        scoreboard.update_scoreboard()
        ball.reset_position()

    # detect collision with right paddle
    if ball.xcor() > 330 and ball.distance(paddle_right) < 50:
        ball.bounce_x()

    # detect collision with right wall
    if ball.xcor() > 390:
        scoreboard.left_score += 1
        scoreboard.update_scoreboard()
        ball.reset_position()

screen.exitonclick()