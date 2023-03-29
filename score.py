from turtle import Turtle
import tkinter

class Score(Turtle):
    cantidad=-1
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.highscore=0
        self.color("white")
        self.penup()
        self.goto(x=0,y=360)
        self.sumar()

    def sumar(self):
        self.clear()
        self.cantidad+=1
        self.write(f"Score = {self.cantidad}", False, "center", ("courier", 15, "normal"))

    def reset(self):
        if self.cantidad>self.highscore:
            self.highscore=self.cantidad
        self.cantidad=0