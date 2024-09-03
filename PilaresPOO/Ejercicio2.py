"""Ejercicio 1

Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__.
Calcular después la suma, resta, multiplicación y división.
Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora."""


class Claculadora():
    def __init__(self):
        self.num1 = int(input("Ingrese el primer valor: "))
        self.num2 = int(input("Ingrese el segundo valor: "))

    def suma(self):
        self.suma = self.num1 + self.num2
        print("La SUMA de los numeros es:",self.suma)
    
    def resta(self):
        self.resta = self.num1 - self.num2
        print("La RESTA de los numeros es:",self.resta)
    
    def multiplicacion(self):
        self.multiplicacion = self.num1 * self.num2
        print("La MULTIPLICACION de los numeros es:",self.multiplicacion)
    
    def divicion(self):
        self.divicion = self.num1 / self.num2
        print("La DIVICION de los numeros es:",self.divicion)
    

calculadora = Claculadora()

calculadora.suma()
calculadora.resta()
calculadora.multiplicacion()
calculadora.divicion()