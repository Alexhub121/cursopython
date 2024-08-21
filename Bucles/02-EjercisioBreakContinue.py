"""Ejercicio 2

Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números,
 pero, solo imprimiendo los números que sean impares"""

print("Hola usuario, ingrese dos numeros para \nmostrar su rango de numeros impares")
num1 = int(input("Ingrese el primer numero:"))
num2 = int(input("Ingrese su segundo numero:"))
print("A continuacion su rango de numero impares")
print("--------------------------------------------")


if num1 < num2:
    for i in range(num1, num2 , + 1):
        if i % 2 == 0:
            continue
        print(i)

elif num1 > num2:
    print("El primer numero tiene que ser menor que el segundo,intenta de nuevo")

elif num1 == num2:
    print("Los numeros son iguales y no se puede mostrar rango,intente de nuevo")

else:
    print("no ingreso datos correctos,intenta de nuevo")

