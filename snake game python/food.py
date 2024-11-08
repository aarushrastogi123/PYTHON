from turtle import Turtle
import random as r

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest') 
        self.refresh()
    def refresh(self):
        x=r.randint(-260,260) 
        y=r.randint(-260,260)
        self.goto(x,y)  