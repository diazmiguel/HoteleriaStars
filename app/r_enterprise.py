from rooms import Room
class Enterprise(Room):
    bed = int
    conference = bool

    def __init__(self, number, available, bed, conference):
        super().__init__(number, available)
        self.bed = bed
        self.conference = conference
