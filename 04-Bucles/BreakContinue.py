for i in range(1 ,11):
    print(i)
    if i == 5: #condicional / aqui pregunta si i es = a 5 para detenerce con el break 
        break #Si la condicion de arriba es true se detendra 

for i in range(1 ,11):
    if i == 6:  #esta es la condicion para que el continue se ejecute 
        continue #Si la condicion es correcta se ejecuta, aqui para en el 6 no lo imprime y lo salta
    print(i)