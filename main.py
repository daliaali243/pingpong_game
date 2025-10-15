from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score


screen=Screen()
screen.bgcolor("black")
screen.setup(width=900,height=600)
screen.tracer(0)
r_paddle = Paddle((410,0))
l_paddle = Paddle((-410,0))

ball=Ball()
score=Score()
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,'w')
screen.onkey(l_paddle.go_down,"s")
default_sleep=0.1
game_on=True
while game_on:
    screen.update()
    time.sleep(default_sleep)
    ball.goto(ball.xcor()+ball.x_move,ball.ycor()+ball.y_move)
    if ball.ycor() > 280 or ball.ycor() <-280 :
        ball.y_move*=-1
    if ball.xcor() > 390 and ball.distance(r_paddle)<=50  or ball.xcor() <-390 and ball.distance(l_paddle)<=50:
        ball.x_move*=-1
        default_sleep*=0.9

    if ball.xcor() > 490:
        ball.goto(0,0)
        ball.x_move*=-1
        default_sleep=0.1
        score.l_piont()
    if ball.xcor() < -490:
        ball.goto(0,0)
        ball.x_move*=-1
        default_sleep=0.1
        score.r_piont()










screen.exitonclick()
