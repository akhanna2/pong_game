from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(5,1)
        self.penup()
        self.speed('fastest')

    def up(self):
        newy = self.ycor() + 20
        self.goto(self.xcor(), newy)

    def down(self):
        newy = self.ycor() - 20
        self.goto(self.xcor(), newy)