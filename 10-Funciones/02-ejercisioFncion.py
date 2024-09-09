"""Ejercicio 2

Escribir una función que reciba un número entero positivo y devuelva su factorial."""

def factorial():
    num = int(input("Ingresa tu numero entero y positivo:"))
    if num > 0: #Pregunta si el numero es mayor a 0
        factorial = 1
        for i in range(1, num + 1): #Empieza en uno y termine en num agregado
            factorial *= i #Hace la multiplicacionm
        print(factorial)
    else:
        print("El numero es negativo")

factorial()