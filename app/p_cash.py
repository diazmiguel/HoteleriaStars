from payment import Payment

class Cash(Payment):
    def __init__(self, total):
        super().__init__(total)