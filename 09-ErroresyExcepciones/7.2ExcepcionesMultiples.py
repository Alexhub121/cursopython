while True:
    try:
        num1 = int(input("Ingrese un numero para dividir entre '100':"))
        resultado = 100 / num1
        print(f"El resultado es: {resultado}")
        break
    except ZeroDivisionError: 
        print("No se puede dividir entre cero")


while True:
    try:
        edad = int(input("Ingrese tu edad"))
        print(f"Tu edad es: {edad}")
        break
    except ValueError: #Sirve para validar un valor
        print("Valor incorrecto")

while True:
    try:
        edad = int(input("Ingrese tu edad"))
        print(f"Tu edad es: {edad}")
        break
    except KeyboardInterrupt: #sirve para cancelar la ejecucion con ctrl+c
        print("\nHas cancelado la ejecucion")
        break