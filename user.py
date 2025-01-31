from bag import Bag

class User:
    def __init__(self, name):
        self.name = name
        self.bag = Bag()

    def __str__(self):
        return f"{self.name}'s Bag"
