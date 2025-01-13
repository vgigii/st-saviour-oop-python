from abc import ABC, abstractmethod

class Dessert(ABC):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        self.toppings = []

    @abstractmethod
    def serve(self):
        pass

    def add_toppings(self, *toppings):
        self.toppings.extend(toppings)

    def __str__(self):
        return "Dessert (Name = " + self.name + ", Price = $" + str(self.price) + ", Toppings = " + str(self.toppings) + ")"