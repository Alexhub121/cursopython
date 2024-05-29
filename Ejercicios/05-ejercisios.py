"""Ejercicio 1

Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas"""

vocal = input("Ingresa una vocal EN MINUSCULAS:")
consonante = input("Ingresa una consonante EN MAYUSCULAS:")

vocal = vocal.upper()
consonante = consonante.lower()

print(f"la consonante fue:\n {consonante}" f"\nLa vocal fue:\n {vocal}")









"""Ejercicio 2

Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:

Te llamas: <nombre>

Tu edad es: <edad>

Eres: <sexo>"""

nombre = (input("Ingrese su nombre:"))
edad = int(input("Ingrese su edad:"))
sexo = (input("Ingrese su sexo (M/F):"))

print(f"Te llamas:\n {nombre}" f"\nTu edad:\n {edad}" f"\nEres:\n {sexo}" )