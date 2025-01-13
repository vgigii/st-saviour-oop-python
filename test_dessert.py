from icecream import IceCream
from frozenyogurt import FrozenYogurt
from sundae import Sundae
from softserve import SoftServe
from dessert import Dessert

def test_dessert():
    
    icecream = IceCream("Vanilla Ice Cream", 2.99, "Vanilla", "Medium")
    frozenyogurt = FrozenYogurt("Berry Yogurt", 3.49, 5, True)
    sundae = Sundae("Chocolate Sundae", 4.99, "Chocolate", "Large")
    softserve = SoftServe("Soft Serve", 1.99, "Smooth")

    desserts = [icecream, frozenyogurt, sundae, softserve]
    for dessert in desserts:
        print(dessert.serve())

    print(isinstance(sundae, IceCream))
    print(isinstance(frozenyogurt, Dessert))

    sundae.add_sundae("Sprinkles", "Cherries")
    print(softserve.serve_cone("Chocolate Chips", "Nuts", cone="waffle"))

    print(str(icecream))
    print(str(frozenyogurt))
    print(str(sundae))
    print(str(softserve))

if __name__ == "__main__":
    test_dessert()