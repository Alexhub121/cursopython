"""Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal"""

vocal = input("Ingresa una vocal en minuscula:")

if vocal.lower() == "a":
    print("La vocal es A")
elif vocal.lower() == "e":
    print("La vocal es E")
elif vocal.lower() == "i":
    print("La vocal es I")
elif vocal.lower() == "o":
    print("La vocal es O")
elif vocal.lower() == "u":
    print("La vocal es U")
else:
    print("No es una vocal")

"""Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52)."""
numero = int(input("Ingrese un valor"))

if numero > 0:
    print(f"el valor absoluto {numero} es {numero}")
else:
    print(f"el valor absoluto de {numero} es {numero * -1}")

print(abs(-5))

