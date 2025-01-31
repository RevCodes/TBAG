class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.revealed = False

    def get_name(self):
        return self.name
    
    def set_name(self, item_name):
        self.name = item_name

    def get_description(self):
        return self.description
    
    def set_description(self, item_description):
        self.description = item_description

    def __eq__(self, other):
        if isinstance(other, Item):
            return self.name == other.name and self.description == other.description
        return False

    def __str__(self):
        if self.revealed:
            return f"{self.name}: {self.description}"
        else:
            return "The item is hidden."

    def reveal(self):
        self.revealed = True


sword = Item("Sword", "A sharp sword made from legandary metal")

""" 
print(Sword)
"""