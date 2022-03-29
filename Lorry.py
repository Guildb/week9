from Vehicle import Vehicle


class Lorry(Vehicle):

    def __init__(self, registration, weight):
        super().__init__(registration, weight)

    def calculatefee(self):
        if self.weight > 8000:
            return 15.00
        return 10.00

