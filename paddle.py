from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, side: str):
        super().__init__()
        self.segments = []
        y_shift = 40
        for _ in range(5):
            segment = Turtle()
            segment.color("white")
            segment.penup()
            segment.shape("square")
            segment.setheading(90)
            if side == "right":
                segment.setposition(470, y_shift)
            elif side == "left":
                segment.setposition(-480, y_shift)
            self.segments.append(segment)
            y_shift -= 20
        self.head = self.segments[0]

    def up(self):
        pass

    def down(self):
        pass
