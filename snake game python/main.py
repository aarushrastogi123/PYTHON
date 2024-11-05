from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
gameover123='''
/*  _____   ___  ___  ___ _____ _____  _   _ ___________  */
/* |  __ \ / _ \ |  \/  ||  ___|  _  || | | |  ___| ___ \ */
/* | |  \// /_\ \| .  . || |__ | | | || | | | |__ | |_/ / */
/* | | __ |  _  || |\/| ||  __|| | | || | | |  __||    /  */
/* | |_\ \| | | || |  | || |___\ \_/ /\ \_/ / |___| |\ \  */
/*  \____/\_| |_/\_|  |_/\____/ \___/  \___/\____/\_| \_| */
'''
screen= Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on=True

while game_is_on:  
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.scoreboard()

    if snake.head.xcor()>280 or snake.head.xcor()<-290 or snake.head.ycor()>280 or snake.head.ycor()<-290:
        game_is_on=False
        print(gameover123)
        
    for n in snake.segments:
        if n==snake.head:
            pass
        elif snake.head.distance(n)<10:
            game_is_on=False
            print(gameover123)
screen.exitonclick()

