from turtle import Turtle
import random
posiciones=range(-350,350)
class Comida(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.penup()
        self.desaparecer()

    def desaparecer(self):
        random_y = random.randint(-380, 380)
        random_x = random.randint(-380, 380)
        self.hideturtle()
        self.goto(x=random_y,y=random_x)
        self.showturtle()