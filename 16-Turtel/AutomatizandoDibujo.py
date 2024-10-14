import turtle

screen = turtle.Screen() #Aqui creamos la ventana
t = turtle.Turtle() #Creamos el puntero
i = 0
"""t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)"""

"""for i in range (4):
    t.fd(100)
    t.rt(90)"""
resultado = input("Quieres imprimir una figura?: ")
if resultado == "si":
    while i <= 100:
        t.circle(i)
        t.speed(10)
        i += 10
        print("La figura se ha creado")

else:
    print("No se imprimio nada")
    quit()

turtle.done()