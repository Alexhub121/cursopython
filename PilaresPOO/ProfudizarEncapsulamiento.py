class A():
    def __init__(self ):
        self._contador = 0
        self._cuenta = 0

    def incrementar(self):
        self._contador += 1

    def cuenta(self):
        return self._contador
    

a = A()



#Cuento el atributo este encapsulado con _ no mandar a llamar como esta ecrito abajo 
# es decir no acceder a el de esa manera y no modificar sus valores , se accederan a ellos por su metodo get y set

# print(a.cuenta)
# a.cuenta = 20
# print(a.cuenta)