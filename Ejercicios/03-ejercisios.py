#Ejercicio 1

"""Realizar un programa que haga el proceso de formula general para 
la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el 
usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para 
que al final muestre el mensaje: “La solución es: <solucion>”"""

from math import sqrt

A = int(input("Ingresa valor de A:"))
B = int(input("Ingresa valor de B:"))
C = int(input("Ingresa valor de C:"))

X1 = 0
X2 = 0

if (B**2)-(4*A*C) < 0:
    print("No se puede raliuzar opor que no se puede sacar raiz de un numero negativo")
else:
    x1 = (-B + sqrt((B**2)-(4*A*C)))/(2*A)
    x2 = (-B - sqrt((B**2)-(4*A*C)))/(2*A)
    print("la solucion es: \nX1=", x1, "\nX2=",x2)
