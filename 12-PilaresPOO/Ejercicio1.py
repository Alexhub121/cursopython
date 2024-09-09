"""Ejercicio 1

Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno.
Definir los métodos para inicializar sus atributos,
imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no."""

class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Nombre: {self.nombre} \nNota: {self.nota}")

    def resultado(self):
        if self.nota >= 7:
            print(f"El estudiante {self.nombre} ha aprobado con una nota de {self.nota}")
        elif self.nota < 7:
            print(f"El estudiante {self.nombre} ha reprobado con una nota de {self.nota}")
        else:
            print(f"El estudiante {self.nombre} no tiene nota")

estudiante = Estudiante("Alex", 10 )
estudiante.imprimir()
estudiante.resultado()