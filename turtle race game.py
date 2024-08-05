from turtle import Turtle , Screen

import random as r

is_race_on= False

turtle_list=[]

screen= Screen()

screen.setup(width=500,height=400)

user_bet=screen.textinput(title="Make your bet!!!",prompt="Which turtle will win the race? Enter a color: ")

y=(20,-10,50,-40,-70,80)

turtle_color=("blue","green","red","purple","yellow","black")

for n in range(0,6):

    new_turtle=Turtle(shape="turtle")
    new_turtle.color(turtle_color[n])
    new_turtle.penup()
    new_turtle.goto(-230,y[n])
    turtle_list.append(new_turtle)

if user_bet:

    is_race_on=True 
   
while is_race_on:

    for turtle in turtle_list: 

        distance_turtle=r.randint(0,10)
        turtle.forward(distance_turtle)

        if turtle.xcor()>230:

            winning_color=turtle.pencolor()

            if winning_color==user_bet:
                print(f"You won. The {winning_color} turtle is the winner!")

            else:
                print(f"You lost. The {winning_color} turtle is the winner!")

            is_race_on=False 

screen.exitonclick()