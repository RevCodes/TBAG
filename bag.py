from item import Item

class Bag:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def show_items(self):
        if self.items:
            print("Your bag contains:")
            for item in self.items:
                print(f"- {item.name}")
        else:
            print("The bag is empty.")

    def has_item(self, item_name):
        return any(item.name.lower() == item_name.lower() for item in self.items)

