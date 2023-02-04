from account import Account
from payment import Payment
#guest = huesped o cliente de nuestro hotel
class Guest(Account):
    payment = Payment("")
    days = int
    def __init__(self, name, services, payment, days):
        super().__init__(name, services)
        self.payment = payment
        self.days = days