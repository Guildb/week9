from Vehicle import Vehicle


class Motorbike(Vehicle):

    def __init__(self, registration, weight):
        super().__init__(registration, weight)

    def calculatefee(self):
        return 3.00
