from turtle import Turtle
class Prueba(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5)
        self.penup()
        self.color("white")
        self.goto(750,0)