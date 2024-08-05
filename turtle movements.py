from turtle import Turtle , Screen

tim=Turtle()
screen = Screen()
def move_forward():
    tim.forward(20)
def move_left():
    a=tim.heading()-20
    tim.setheading(a)
def move_backwards():
    tim.backward(20)
def move_right():
    b=tim.heading()+20
    tim.setheading(b)
def clear_screen():
    tim.clear()
    tim.teleport(0,0)
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="a",fun=move_left)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="d",fun=move_right)
screen.onkey(key="c",fun=clear_screen)
screen.exitonclick()
