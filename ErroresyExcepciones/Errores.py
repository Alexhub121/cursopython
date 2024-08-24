"""while True: #Esto hace que el programa se repite

    try:
        edad = int(input('Ingrese su edad:'))
        print("Tu edad es:",edad)
        break #Aqui termina el bucle
    except:
        print("Ingresaste un valor erroneo")
    finally:
        print("Fin del programa")#Este bloque se ejecuta siempre, independientemente de si"""


while True:

    try:
        nombre = str(input("Ingresa tu nombre:"))
        edad = int(input("Ingresa tu edad:"))
        print(f"Hola {nombre} tu edad es:{edad}")
        break #Aqui termina el bucle
    except:
        print("Ingresa los datos que se te piden :)")
        continue

while True:
    try:
        continuar = input("Desea agregar nuevos datos? (s/n)").lower()
        
        if continuar == "s":
            nombre = str(input("Ingresa tu nombre:"))
            edad = int(input("Ingresa tu edad:"))
            print(f"Hola {nombre} tu edad es:{edad}")
            
        elif continuar == "n":
            print("Gracias por utilizar el programa")
            break
    except:
        print("Ingresa los datos que se te piden")
        continue