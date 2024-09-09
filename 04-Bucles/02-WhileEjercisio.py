"""Ejercicio 2

Escribir un programa que pregunte al usuario su edad y muestre por 
pantalla todos los años que ha cumplido (desde 1 hasta su edad)."""

edad = int(input("Ingrese su edad:")) #usuario ingresa su edad
i = 0 #Guardamos el punto de inicio
while i < edad: #El bucle se repetira hasta que i sea mayor que edad
    i += 1 #Va sumando de uno en uno y mostrando en patalla hasta llegar a la edad ingresada 
    print(f"Estos son los años que a cumplido:{i}")  # imprime los años que ha cumplido el usuario