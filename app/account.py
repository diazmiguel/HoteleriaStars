#Clase principal
from rooms import Room
#Aqui tenemos Staff y Huesped
class Account:
    id = int
    name = str
    services = Room("","")

    def printData(self):
        print("Nombre= "+ self.name, " Un cliente")
        return 
    #email = str Para despues!
    def __init__(self, name, services):
        self.name = name
        self.services = services
        