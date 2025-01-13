from dessert import Dessert


class FrozenYogurt(Dessert):
   def __init__(self, name: str, price: float, tartness_level: int, probiotics: bool):
       super().__init__(name, price)
       self.tartness_level = tartness_level
       self.probiotics = probiotics

   def serve(self):
       return "Serving frozen yogurt with tartness level " + str(self.tartness_level) + "."

   def __str__(self):
       return "FrozenYogurt (Name = " + self.name + ", Price = $" + str(self.price) + ", Tartness level = " + str(self.tartness_level) + ", Probiotics = " + str(self.probiotics) + ", Toppings = " + str(self.toppings) + ")"
