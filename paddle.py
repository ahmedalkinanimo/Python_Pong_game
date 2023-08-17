from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, side: str):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        if side == "right":
            self.goto(360, 0)
        elif side == "left":
            self.goto(-360, 0)

    def up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor()+20)

    def down(self):
        if self.ycor() > -220:
            self.goto(self.xcor(), self.ycor()-20)
