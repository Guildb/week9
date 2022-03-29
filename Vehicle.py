from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, registration, weight):
        self.registration = registration
        self.weight = weight

    @abstractmethod
    def calculatefee(self):
        pass
