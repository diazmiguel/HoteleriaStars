
class Room:
    id = int
    number= int
    available = bool #Nos indica si esta ocupado
    # e person = Account("","")
    #person = account

 #Metodo constructor
    def __init__(self, number, available):
        self.number= number
        self.available= available
        #self para apuntar a las variable de la clase

    #def printDataRoom():
    #    print("Numero: "+number+ "Ocupado:"+ services+"\n Nombre: "+name+"Dni: "+dni)

