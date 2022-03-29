


class Bridge:

    def __init__(self, maxweight):
        self.traffic = []
        self.maxweigh = maxweight

    def calcTotalWeight(self):
        totalweight = 0
        for i in self.traffic:
            totalweight += i.weight
        return totalweight

    def add(self, vehicle):
        totalweight = self.calcTotalWeight() + vehicle.weight
        if len(self.traffic) <= 20 and totalweight <= self.maxweigh:
            self.traffic.append(vehicle)
            return True
        return False

    def remove(self, registration):
        for i in self.traffic:
            if i.registration == registration:
                self.traffic.remove(i)
                return True
        return False