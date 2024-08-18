"""Ejercicio 1

En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y 
esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

[20, 50, "Curso", 'Python', 3.14]"""


lista1 = [20, 50, "Curso", 'Python', 3.14]
print(lista1)
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
lista1[0] = num1
lista1[1] = num2
print(lista1)  # [num1, num2, "Curso", 'Python',


'''Ejercicio 2

Escribe una lista que tenga los números de 1 al 10. Luego, 
debes hacer que los datos que están en las posiciones 4, 7 y 9 sean multiplicados por 2;
por último, mostrar la lista nueva con los nuevos datos'''


lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista2)
print("-----------------------------------")

lista2[4] *= 2
lista2[7] *= 2
lista2[9] *= 2
print(lista2)