"""Ejercicio 1

Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura;
y la otra el area de un circulo con argumento de radio"""

def cuadrado(base , altura):
    area = base * altura 
    return area

print(cuadrado(10 , 10))

def circulo(radio):
    area = 3.14 * (radio ** 2)
    return area

print(float(circulo(10)))