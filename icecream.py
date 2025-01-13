from dessert import Dessert


class IceCream(Dessert):
   def __init__(self, name: str, price: float, flavor: str, size: str):
       super().__init__(name, price)
       self.flavor = flavor
       self.size = size

   def serve(self):
       return "Serving " + self.size + " " + self.flavor + " ice cream."

   def scoop(self):
       return "Scooping a " + self.size + " " + self.flavor + " ice cream."

   def __str__(self):
       return "IceCream (Name = " + self.name + ", Price = $" + str(self.price) + ", Flavor = " + self.flavor + ", Size = " + self.size + ", Toppings = " + str(self.toppings) + ")"

