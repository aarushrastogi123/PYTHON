from turtle import Turtle
x=[(0,0),(-20,0),(-40,0)]
moveby=20
up=90
down=270
left=180
right=0

class Snake():

    def __init__(self):
        self.segments=[]
        self.createsnake()
        self.head=self.segments[0]
    
    def createsnake(self):
        for n in x:
            self.add_segment(n)

    def add_segment(self, n):
            tim=Turtle(shape="square")
            tim.color("white")
            tim.penup() 
            tim.goto(n)
            self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(moveby)

    def up(self):
        if self.segments[0].heading() !=down:
            self.segments[0].setheading(up)
    def down(self):
        if self.segments[0].heading() !=up:
            self.segments[0].setheading(down)
    def left(self):
        if self.segments[0].heading() !=right:
            self.segments[0].setheading(left)
    def right(self):
        if self.segments[0].heading()!=left:
            self.segments[0].setheading(right)
            
    