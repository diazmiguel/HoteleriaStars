from rooms import Room
class Basic(Room):
    bed = int #var privada __bed
    def __init__(self, number, available, bed):
        super().__init__(number, available)
        self.bed = bed