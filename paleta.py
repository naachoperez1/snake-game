from turtle import Turtle

class self(Turtle):

    def __init__(self, posicion):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(posicion)

    def arriba(self):
        actual_y=self.ycor()
        self.goto(y=actual_y + 40, x=self.xcor())



    def abajo(self):
        actual_y=self.ycor()
        self.goto(y=actual_y - 40, x=self.xcor())