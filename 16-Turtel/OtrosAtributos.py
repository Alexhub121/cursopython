import turtle

s = turtle.Screen()
t = turtle.Turtle()

"""t.begin_fill() #Inicia rellenado
t.circle(100) #Lo que este dentro es lo que se rellenara 
t.end_fill()#Termina rellenado

t.begin_fill()
t.color("white", "white") #En esta parte hace que la tortuga y el circulo se pinten de blanco
t.circle(50)
t.end_fill()"""

t.shape("turtle") #Figura del puntero 
"""t.shape("arraow") #Figura del puntero 
t.shape("circle") #Figura del puntero 
t.shape("square") #Figura del puntero 
t.shape("triangle") #Figura del puntero 
t.shape("calssic") Figura del puntero """

t.penup() #Esto es para que deje de dibujar
t.fd(100)
t.pendown() #Esto es para que vuelva dibujar
t.fd(100)
t.penup() #Esto es para que deje de dibujar
t.fd(100)
t.pendown() #Esto es para que vuelva dibujar
t.fd(100)

t.undo()#Esto es como un ctrl + z
t.clear()#Esto es para limpiar  la pantalla
t.reset()# Se reinicia el programa

t.fd(100)
t.stamp()#Deja un sello o marca de agua 
t.fd(100)


turtle.done()