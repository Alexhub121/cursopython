"""Ejercicio 2

Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al usuario un número,
el que haya ingresado, es la letra que debe imprimir el programa"""

tupla = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'w', 'x', 'y', 'z')
numero = int(input("Ingrese un número del 1 al 25 para saber la letra : "))
print(tupla[numero - 1])