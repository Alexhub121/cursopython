"""Ejercicio 1
Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero"""

numero = int(input("Ingrese el numero:")) #Aqui pide al usuario el numero
i = 0  #Servira para guardar y actualizar el dato 
multi = 0 #Servira para guardadr y actualizar los datos de la multiplicacion 

while i <= 10: #Aqui se determina la regla de que i no sea mayor a 10 por que sera el numero maximo que queremos multiplicar
    multi = numero * i #Aqui hace el procedimiento y actualizacion de los datos 
    print(f"{numero} x {i} = {multi}") #imprime en pantalla el resultado hasta que el while sea true
    i += 1  # incrementa el valor de i en 1 en cada iteración