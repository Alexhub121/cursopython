class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0

    @property #Aqui le decimos al programa que esto sera tomado como un metodo get para llamarlo como un atributo Este es el metodo get para poder acceder al atributo de forma correcta
    def cuenta(self): #Es buena practica agregar el mismo nombre al get que el del atributo
        return self._cuenta #Este es el atributo
    
    @cuenta.setter
    def cuenta(self, cuenta): #Este es el metodo set para poder modificar el atributo
        self._cuenta = cuenta #Este es el atributo

    @property #Aqui le decimos al programa que esto sera tomado como un metodo get para llamarlo como un atributo Este es el metodo get para poder acceder al atributo de forma correcta
    def contador(self): #Es buena practica agregar el mismo nombre al get que el del atributo
        return self._contador #Este es el atributo
    
    @contador.setter
    def contador(self, contador): #Este es el metodo set para poder modificar el atributo
        self._contador = contador



a = A()
print(a.cuenta) 
a.cuenta = 20
print(a.cuenta) 
print(a.contador) 
a.contador = 50
print(a.contador)


#El metodo get solo se coloca y el set se modifica valor