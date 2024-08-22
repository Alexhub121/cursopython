def numeros():
    num1 = int(input("Ingresa un numero:"))
    num2 = int(input("Ingresa un numero:"))

    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0

print(numeros())