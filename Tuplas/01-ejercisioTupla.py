"""Ejercicio 1

Escribir una tupla con los meses del año,
luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla"""


tupla = ("Enero", "ferero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
mes = int(input("Ingrese el número del mes que desea mostrar: "))
print(tupla[mes - 1])
