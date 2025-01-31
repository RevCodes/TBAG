from item import Item
from bag import Bag
class Character:

    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = ""

    def describe(self):

        print ( self.name + " is here!")
        print ( self.description)

    def set_conversation (self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name} says]: {self.conversation}")
        else:
            print(self.name + " doesn't want to talk to you")

    
    def fight(self, combat_item):
        print(self.name + "doesn't want to fight with you")

        return True
    
class Enemy(Character):
    
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            return True
        
        else:
            
            print(self.name + " Defeats you!")
            return False

class Friend(Character):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.gift = None

    def set_gift(self, friendly_gift):
        self.gift = friendly_gift
    
    def get_gift(self):
        return self.gift

    def give_gift(self, user_bag):
        if self.gift:
            user_bag.add_item(self.gift)
            print(f"{self.name} gave {self.gift.name} to the user")
            self.gift = None
        else:
            print(f"{self.name} has no gift to give.")

    def talk(self, user_bag):
        super().talk()
        self.give_gift(user_bag)
        
        
    