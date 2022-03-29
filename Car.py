from Vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, registration, weight):
        super().__init__(registration, weight)

    def calculatefee(self):
        if self.weight <= 1590:
            return 5.00
        extra = self.weight - 1590
        multiplier = int(extra / 100)
        actualFee = 5.00 + 0.10 * multiplier
        return actualFee
