from rooms import Room
class Premier(Room):
    sommier= int
    buffet = bool

    def __init__(self, number, available, sommier, buffet):
        super().__init__(number, available)
        self.sommier= sommier
        self.buffet= buffet
    


    