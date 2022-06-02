from turtle import Turtle, Screen, onkeypress
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.title('Pong')
screen.screensize(800, 600, bg='black')
screen.tracer(0)

right_paddle = Paddle()
right_paddle.goto(350, 0)

left_paddle = Paddle()
left_paddle.goto(-350,0)

ball = Ball()

screen.onkeypress(right_paddle.up, 'Up')
screen.onkeypress(right_paddle.down, 'Down')

screen.onkeypress(left_paddle.up, 'w')
screen.onkeypress(left_paddle.down, 's')



scoreboard = Scoreboard()

while True:
    time.sleep(0.07)
    screen.listen()
    game_on = True
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if right_paddle.distance(ball) < 50 and ball.xcor() > 320:
        ball.x_bounce()

    if left_paddle.distance(ball) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.update_l()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.update_r()
    
    if scoreboard.l_score == 5:
        scoreboard.winner_l()
        game_on = False

    if scoreboard.r_score == 5:
        scoreboard.winner_r()
        game_on = False

    if game_on == False:
        ball.stop()
        scoreboard.replay(screen)
        game_on = True

    

screen.exitonclick()