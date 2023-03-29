from turtle import  Screen
from comida import Comida
from snake import Snake
from score import Score
import time
screen=Screen()
screen.setup(width=800,height=800)
screen.bgcolor('black')
screen.title('Fortnite')
screen.tracer(0)
screen.listen()

snake=Snake()
comida=Comida()
score=Score()

seguir=True
while seguir:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.cabeza.distance(comida)<15:
        comida.desaparecer()
        score.sumar()
        snake.crecer()
    if snake.cabeza.xcor()>760 or snake.cabeza.ycor()>400 or snake.cabeza.xcor()<-760 or snake.cabeza.ycor()<-400:
        seguir=False
    for segmento in snake.segmentos[1:]:
        if snake.cabeza.distance(segmento)<10:
            seguir=False


screen.exitonclick()
