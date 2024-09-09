def valores():
    global num1 ,num2 #Esto sirve para acceder a las variables desde fuera
    num1 = 110
    num2 = 40
    resultado = num1 + num2
    return resultado

print(valores())


resta = num1 - num2 #Aqui aaccedemos a la variable desde fuera por que estamos fuera de el def
print(resta)