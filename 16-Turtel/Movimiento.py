import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.goto(100,100)
t.goto(-100,100)
t.home()#Aqui regresa al punto 0,0

#Dibujar cuadrado a la derecha
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)

#Dibujar cuadrado a la izquierada
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)

turtle.done()