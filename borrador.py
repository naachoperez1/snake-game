paleta=Turtle()
paleta.setx(730)
paleta.shape("square")
paleta.color("white")
paleta.shapesize(stretch_wid=5, stretch_len=1)
paleta.penup()
paleta.speed("fastest")


def arriba():
    sube=paleta.ycor()
    paleta.goto(x=paleta.xcor(),y=sube+15)

def abajo():
    baja=paleta.ycor()
    paleta.goto(x=paleta.xcor(),y=baja-15)