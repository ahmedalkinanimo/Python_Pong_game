from turtle import Screen
from paddle import Paddle
import time

if __name__ == '__main__':
    screen = Screen()
    screen.bgcolor("black")
    screen.title("Pong Game")
    screen.setup(1000, 600)
    screen.tracer(0)

    left_paddle = Paddle("left")
    right_paddle = Paddle("right")

    screen.listen()
    screen.onkey(right_paddle.up, "Up")
    screen.onkey(right_paddle.down, "Down")
    screen.onkey(left_paddle.up, "w")
    screen.onkey(left_paddle.down, "s")

    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)

    screen.exitonclick()


