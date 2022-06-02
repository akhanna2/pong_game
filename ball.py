from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.speed('fastest')
        self.xmove = 10
        self.ymove = 10

    def move(self):
        newx = self.xcor() + self.xmove
        newy = self.ycor() + self.ymove
        self.goto(newx, newy)

    def y_bounce(self):
        self.ymove *= -1

    def x_bounce(self):
        self.xmove *= -1

    def reset_position(self):
        self.goto(0,0)
        self.x_bounce()

    def stop(self):
        #self.hideturtle()
        self.goto(0,0)