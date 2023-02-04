from payment import Payment

class Card(Payment):
    numberCard = int

    def __init__(self, total, numberCard):
        super().__init__(total)
        self.numberCard = numberCard
