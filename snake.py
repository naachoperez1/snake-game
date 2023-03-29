from turtle import Turtle,Screen
s=Screen()

STARTING_POSITION= [0, -20, -40]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.segmentos = []

        for i in range(3):
            nuevo_segmento = Turtle("square")
            nuevo_segmento.color("white")
            nuevo_segmento.penup()
            nuevo_segmento.setx(STARTING_POSITION[i])
            self.segmentos.append(nuevo_segmento)

        self.cabeza=self.segmentos[0]


    def derecha(self):
        if self.cabeza.heading()!=180:
            self.cabeza.setheading(0)

    def izquierda(self):
        if self.cabeza.heading() != 0:
            self.cabeza.setheading(180)

    def arriba(self):
        if self.cabeza.heading() != 270:
            self.cabeza.setheading(90)

    def abajo(self):
            if self.cabeza.heading() != 90:
                self.cabeza.setheading(270)

    def move(self):
        for seg_num in range(len(self.segmentos) - 1, 0, -1):
            new_x = self.segmentos[seg_num - 1].xcor()
            new_y = self.segmentos[seg_num - 1].ycor()
            self.segmentos[seg_num].goto(new_x, new_y)
        self.segmentos[0].forward(MOVE_DISTANCE)
        s.onkey(self.derecha,'Right')
        s.onkey(self.izquierda, "Left")
        s.onkey(self.arriba, 'Up')
        s.onkey(self.abajo, 'Down')

    def crecer(self):
        nuevo_s = Turtle("square")
        nuevo_s.goto(x=self.segmentos[-1].xcor(),y=self.segmentos[-1].ycor())
        nuevo_s.color("white")
        nuevo_s.penup()
        self.segmentos.append(nuevo_s)






