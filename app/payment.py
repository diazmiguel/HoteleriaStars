class Payment:
    id = int
    total = int
    
    def __init__(self, total):
        self.total = total