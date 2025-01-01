from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen= Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)
   
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball= Ball()
score=Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,'Up')
screen.onkey(r_paddle.go_down,'Down')
screen.onkey(l_paddle.go_up,'w')
screen.onkey(l_paddle.go_down,'s')

game_is_on=True
while game_is_on:
    time.sleep(ball.speedrun)
    screen.update()
    ball.move()
    #Detect collision with the wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.wall_bounce()

    #detect collision with the paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.paddle_bounce()
    
    #detect when r paddle misses
    if ball.xcor()>410:
        ball.reset_position()
        score.l_point()

    #detect when l paddle misses
    if ball.xcor()<-410:
        ball.reset_position()
        score.r_point()
        
screen.exitonclick()