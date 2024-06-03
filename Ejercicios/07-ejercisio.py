"""Ejercicio 1

Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman.
 Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman."""

palabra1 = input("Ingrese la primer palabra:")
palabra2 = input("Ingrese la segunda palabra:")

if palabra1[-3 : ] == palabra2[-3 : ]:
    print("Las palabras terminan con los mismos tres caracteres")
else:
    print("las palabras NO riman")

"""Ejercicio 2

Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A 
por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. Según el candidato elegido 
(A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. 
Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”."""

votar = input("Ingrese A,B,C para votar por un partido:")

A = "partido rojo"
B = "partido verde"
C = "partido azul"

if A:
    print(f"Usated a votado por el partido {A}")
elif B:
    print(f"Usated a votado por el partido {B}")
elif C:
    print(f"Usated a votado por el partido {C}")
else:
    print("Opción errónea")