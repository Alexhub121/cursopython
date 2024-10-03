import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor("red")#Color de backgaround
s.title("Proyecto 1")#Titulo de la ventana

t.shapesize(3, 3, 3)#Tamano de la tortuga
t.fillcolor("white")#Color de la tortuga

t.pencolor("white")#Color de la linea
t.fd(100)

t.color("white", "blue") #Color tortuga y linea
t.rt(90)
t.fd(100)
t.pensize(10)#Grosor de la linea
t.fd(50)

turtle.done()