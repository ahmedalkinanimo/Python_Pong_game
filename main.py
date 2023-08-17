from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

if __name__ == '__main__':
    screen = Screen()
    screen.bgcolor("black")
    screen.title("Pong Game")
    screen.setup(800, 600)
    screen.tracer(0)

    left_paddle = Paddle("left")
    right_paddle = Paddle("right")
    game_ball = Ball()
    score = ScoreBoard()

    screen.listen()
    screen.onkey(right_paddle.up, "Up")
    screen.onkey(right_paddle.down, "Down")
    screen.onkey(left_paddle.up, "w")
    screen.onkey(left_paddle.down, "s")

    speed = 0.1
    game_on = True
    while game_on:
        screen.update()
        time.sleep(speed)
        game_ball.move()

        # collision with wall
        if game_ball.ycor() > 280 or game_ball.ycor() < -280:
            game_ball.bounce_y()

        # collision with paddle
        if (game_ball.distance(right_paddle) < 50 and game_ball.xcor() > 340) or (game_ball.distance(left_paddle) < 50 and game_ball.xcor() < -340):
            game_ball.bounce_x()
            speed *= 0.9

        # right paddle miss a ball
        if game_ball.xcor() > 380:
            game_ball.reset_position()
            speed = 0.1
            score.l_point()

        # right paddle miss a ball
        if game_ball.xcor() < -380:
            game_ball.reset_position()
            speed = 0.1
            score.r_point()

    screen.exitonclick()



