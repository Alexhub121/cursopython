import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.circle(10)
t.speed(10)
t.circle(20)
t.speed(10)
t.circle(50)#Circulo
t.speed(10)#Velocidad
t.dot(30)#Circulo relleno

t.hideturtle()#Esconde la tortuga
t.circle(40)

t.showturtle()#Hace visible la tortuga

t.setx(100)
t.sety(-50)

turtle.done()