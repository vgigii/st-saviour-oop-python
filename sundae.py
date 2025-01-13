from icecream import IceCream


class Sundae(IceCream):
   def __init__(self, name: str, price: float, flavor: str, size: str):
       super().__init__(name, price, flavor, size)
      
   def add_syrup(self, syrup: str):
       self.toppings.append(syrup)

   def add_sundae(self, *args):
       self.toppings.extend(args)

   def __str__(self):
       return "Sundae (Name = " + self.name + ", Price = $" + str(self.price) + ", Flavor = " + self.flavor + ", Size = " + self.size + ", Toppings = " + str(self.toppings) + ")"

