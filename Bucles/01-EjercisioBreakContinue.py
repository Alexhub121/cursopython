"""Ejercicio 1

Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros
 y mostrar el rango de numeros entre ambas cifras"""

print("Hola usuario bienvenido""\nLos numeros del 1 al 10 son:")

for i in range(1 , 11):
    print(i)

print("-----------------------")

print("Ahora ingresa dos numeros para mostrar su rango")
num1 = int(input("Ingresa el primer numero:"))
num2 = int(input("Ibngresa tu segundo numero:"))

if num1 < num2:
    print(f"El rango entre los numeros {num1} y {num2} son:")
    for i in range(num1, num2 +1):
        print(i)
elif num1 > num2:
    print("Si quieres obtener el rango de tus numeros, el primero tiene que ser menor que el segundo!!")
else:
    print("Tus numeros son iguales o ingresaste otro dato,intenta de nuevo")
    