from dessert import Dessert


class SoftServe(Dessert):
   def __init__(self, name: str, price: float, texture: str):
       super().__init__(name, price)
       self.texture = texture

   def serve(self):
       return "Serving soft-serve with " + self.texture + " texture."

   def swirl(self):
       return "Swirling soft-serve ice cream with " + self.texture + " texture."

   def serve_cone(self, *args, **kwargs):
       cone_type = kwargs.get("cone", "regular")
       return "Serving soft-serve in a " + cone_type + " cone with toppings: " + ", ".join(args) + "."

   def __str__(self):
       return "SoftServe (Name = " + self.name + ", Price = $" + str(self.price) + ", Texture = " + self.texture + ", Toppings = " + str(self.toppings) + ")"
