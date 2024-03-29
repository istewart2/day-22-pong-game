from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.setposition(position)

    def move_up(self):
        new_y_cor = self.ycor() + 20
        self.goto(self.xcor(), new_y_cor)

    def move_down(self):
        new_y_cor = self.ycor() - 20
        self.goto(self.xcor(), new_y_cor)
