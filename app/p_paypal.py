from payment import Payment

class Paypal(Payment):
    email = str

    def __init__(self, total, email):
        super().__init__(total)
        self.email = email