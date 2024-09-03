"""Ejercicio 1

Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro.
Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes.
Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno"""


class FabricaCarros():
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

class Moto(FabricaCarros):
    def moto(self):
        print(f"Espesificaciones de la MOTO \nLlantas: {moto.llantas}, Color: {moto.color}, Precio: {moto.precio}")
        
    

class Carro(FabricaCarros):
    def carro(self):
        print(f"Espacificaciones de el CARRO \nllantas: {carro.llantas}, color: {carro.color}, precio: {carro.precio}")
        

moto = Moto(2, "rojo", 500)
moto.moto()

carro = Carro(4, "Verde", 10000)
carro.carro()
