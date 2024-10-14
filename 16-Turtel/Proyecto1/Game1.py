import turtle
import random


screem = turtle.Screen() #Aqui creamos la ventana
screem.title("PRIMER JUEGO")
screem.bgcolor("gray")
t1 = turtle.Turtle() #Creamos el puntero
t2 = turtle.Turtle()

#JUGADOR 1
t1.hideturtle()
t1.shape("turtle")
t1.color("green", "green")
t1.shapesize(2,2,2)
t1.pensize(3)

#JUGADOR2
t2.hideturtle()
t2.shape("turtle")
t2.color("blue", "blue")
t2.shapesize(2,2,2)
t2.pensize(3)

#MOVIMIENTO JUGADOR 1
t1.penup()
t1.goto(300 , 200)
t1.pendown()
t1.circle(50)
t1.penup()
t1.goto(-300 , 250)
t1.showturtle()

#MOVIMIENTO JUGAROD 2
t2.penup()
t2.goto(300 , -190)
t2.pendown()
t2.circle(50)
t2.penup()
t2.goto(-300 , -150)
t2.showturtle()



turtle.done()