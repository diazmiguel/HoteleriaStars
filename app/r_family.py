from rooms import Room
class Family(Room):
    bed = int
    cradle = int #Cunas para bebe
    ninieras = bool 

    def __init__(self, number, available, bed, ninieras):
        super().__init__(number, available)
        self.bed = bed
        self.ninieras = ninieras