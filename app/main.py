#inicio
from account import Account #borrar
from rooms import Room #borrar
#Tipos de personas
from a_staff import Staff
from a_guest import Guest
#Tipos de servicios 
from r_premier import Premier
#Tipos de pagos
from p_card import Card

#importamos las Account(personas) y Room(habitaciones)

#Menu para la inicializacion
if __name__ == "__main__":
    print('Menu')
    client = Account('Fernando Guerrero', Room(1,False))
    print(vars(client))
    print(vars(client.services))

    print('MENU ')
    staff1= Staff('Juan Heraldo',Premier(2,False,2,True),2134,'Resepcionista')
    print(vars(staff1))
    print(vars(staff1.services))

    print('cliente')
    client2 = Guest("Javier Maslow", Premier(3,False,1,True),Card(2130,67676767),32)
    print(client2.name)
    print(vars(client2.services), vars(client2.payment))
    client2.printData()

