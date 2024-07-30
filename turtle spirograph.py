from turtle import Turtle
tim=Turtle()
tim.shape("arrow")
import random as r
colors=["cyan",'yellow',"black","red","pink","green","orange","indigo","blue",'lime',"brown",'dark grey','hot pink']
def draw_spirograph(size):
    for n in range(int(360/size)):
        tim.circle(radius=100)
        tim.setheading(tim.heading()+size)
        n=+1
        tim.speed(30)
        tim.color(r.choice(colors))
draw_spirograph(5)

screen=Turtle.screen()
screen.exitonclick()