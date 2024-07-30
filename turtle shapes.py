from turtle import Turtle 
tim=Turtle()
tim.shape("turtle")

#  WAY ONE
import random as r
colors=["cyan",'yellow',"black","red","pink","green","orange","indigo","blue",'lime',"brown",'dark grey','hot pink']

def shapes(num_sides):
    angle=360/num_sides
    for a in range(num_sides):
        tim.forward(100)
        tim.right(angle)
for shape_sides in range(3,11):
    tim.color(r.choice(colors))
    shapes(shape_sides)

# WAY TWO

def tri():
    for n in range(0,3):
        tim.color("violet")
        tim.fillcolor("violet")
        tim.right(120)
        tim.forward(100)
        n+=1
def sq():
    for n in range(0,4):
        tim.color("indigo")
        tim.fillcolor("indigo")
        tim.right(90)
        tim.forward(100)
        n+=1
def pen():
    for n in range(0,5):
        tim.color("blue")
        tim.fillcolor("blue")
        tim.right(72)
        tim.forward(100)
        n+=1
def hex():
    for n in range(0,6):
        tim.color("green")
        tim.fillcolor("green")
        tim.right(60)
        tim.forward(100)
        n+=1
def hep():
    for n in range(0,7):
        tim.color("yellow")
        tim.fillcolor("yellow")
        tim.right(51.4)
        tim.forward(100)
        n+=1
def oct():
    for n in range(0,8):
        tim.color("orange")
        tim.fillcolor("orange")
        tim.right(45)
        tim.forward(100)
        n+=1
def nona():
    for n in range(0,9):
        tim.color("red")
        tim.fillcolor("red")
        tim.right(40)
        tim.forward(100)
        n+=1
def deca():
    for n in range(0,10):
        tim.color("pink")
        tim.fillcolor("pink")
        tim.right(36)
        tim.forward(100)
        n+=1
for n in range(0,1):
    tri()
    sq()
    pen()
    hex()
    hep()
    oct()
    nona()
    deca()
