class A():
    def __init__(self):
        self.contador = 0

    def incrementar(self):
        self.contador += 1

    def cuenta(self):
        return self.contador
    
class B():
    def __init__(self):
        self.__contador = 0

    def incrementar(self):
        self.___contador += 1

    def cuenta(self):
        return self.___contador #El doble _ sirve para encapsular los atributos y solo se acceda desde la class


print("----------OBJETO 1----------")
a = A()
print(a.cuenta())  # 0 #como es un metodo se ponen los parentesis 
a.incrementar()
print(a.cuenta())  # 1


print("----------OBJETO 2----------")
b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())  # 1
print(b.__contador())