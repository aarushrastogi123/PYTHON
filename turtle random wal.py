from turtle import Turtle
import random as r
colors=["cyan",'yellow',"black","red","pink","green","orange","indigo","blue",'lime',"brown",'dark grey','hot pink']
f=int(input("Range of random walk: "))
a=Turtle()
a.shape("arrow")
a.pensize(1)
directions=[0,90,180,270]

for n in range (0,f):
    a.forward(30)
    a.setheading(r.choice(directions))
    a.color(r.choice(colors))
    a.speed(20)
    n+=1


