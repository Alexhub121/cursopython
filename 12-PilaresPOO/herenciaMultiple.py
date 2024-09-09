class A(): #Class Padre
    def primera(self):
        return "Hola soy la clase A"
    
class B(): #Class Padre
    def segunda(self):
        return "Hola soy la clase B"
    
class C(A , B): #Asi realizamos una herencia multiple en una class
    def tercera(self):
        pass

c = C()
print(c.primera()) #Imprime Hola soy la clase A
print(c.segunda()) #Imprime Hola soy la clase B