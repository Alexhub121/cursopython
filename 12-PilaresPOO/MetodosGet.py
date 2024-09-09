class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0

    @property #Aqui le decimos al programa que esto sera tomado como un metodo get para llamarlo como un atributo Este es el metodo get para poder acceder al atributo de forma correcta
    def cuenta(self): #Es buena practica agregar el mismo nombre al get que el del atributo
        return self._cuenta #Este es el atributo
    
    @property #Aqui le decimos al programa que esto sera tomado como un metodo get para llamarlo como un atributo Este es el metodo get para poder acceder al atributo de forma correcta
    def contador(self): #Es buena practica agregar el mismo nombre al get que el del atributo
        return self._contador #Este es el atributo

a = A()
print(a.cuenta) #Aqui llamamos al metodo get de cuenta como si fuera ub atributo
print(a.contador) #Aqui llamamos al metodo get de contador como si fuera un atributo