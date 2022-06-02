from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()
        
    def update(self):
        self.goto(-100, 250)
        self.write(self.l_score, align='center', font=('courier',50,'normal'))
        self.goto(100, 250)
        self.write(self.r_score, align='center', font=('courier',50,'normal'))

    def update_l(self):
        self.clear()
        self.l_score += 1
        self.update()

    def update_r(self):
        self.clear()
        self.r_score += 1
        self.update()

    def winner_l(self):
        self.goto(0,0)
        self.write('Left Won!', align='center', font=('courier',90,'normal'))

    def winner_r(self):
        self.goto(0,0)
        self.write('Right Won!', align='center', font=('courier',90,'normal'))

    def replay(self, screen):
        replay = screen.textinput('replay', 'start again (y/n):  ')
        if replay == 'y':
            self.l_score = 0
            self.r_score = 0
            self.clear()
            self.update()
        else:
            screen.bye()