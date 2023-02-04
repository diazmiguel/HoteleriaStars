from account import Account

class Staff(Account):
    salary = int
    type = str

    def __init__(self, name, services, salary, type):
        super().__init__(name, services)
        self.salary = salary
        self.type = type