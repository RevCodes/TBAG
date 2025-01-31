from character import Enemy
from character import Friend
from room import Room
from item import Item
from bag import Bag

user_name = input("Enter your name: ")
print(f"Welcome, {user_name}! You can type 'talk' to interact with characters, north, east, south and west to move to other rooms, 'fight' to engage enemies in combat, or 'i' to check your bag. Let's begin your adventure!\n")
user_bag = Bag()

sword = Item("Sword", "A sharp sword made from legendary metal")

kitchen = Room()
kitchen.set_name("kitchen")
kitchen.set_description("A cold dark room with rats inside")

ballroom = Room()
ballroom.set_name("ballroom")
ballroom.set_description("A large beautiful room with a chandelier hanging from the ceiling, an old piano, and many chairs scattered around the room. Perhaps there was a recent gathering here?")

dining_hall = Room()
dining_hall.set_name("dining hall")
dining_hall.set_description("A long room full of tables and chairs. Leftover food can be seen on the tables, I wonder if it's still warm?")

mine_tunnel = Room()
bedroom = Room()

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

caitlyn = Friend("Caitlyn", "The Sheriff")
caitlyn.set_conversation(f"Hello {user_name}, This might help you on your adventure.")
caitlyn.set_gift(sword)
dining_hall.set_character(caitlyn)

twitch = Enemy("Twitch", "The fat rat")
twitch.set_conversation("SNEAKY SNEAKY, LET'S FIGHT")
twitch.set_weakness("Sword")
kitchen.set_character(twitch)

current_room = ballroom
current_room.get_details()

while True:
    command = input("> ").lower()
    
    if command == "talk":
        inhabitant = current_room.get_character()
        if inhabitant is not None:
            if isinstance(inhabitant, Friend):
                inhabitant.talk(user_bag)  
                print("\nYou can now head to the kitchen by going north or back to the ballroom by going west.")
            else:
                inhabitant.talk()
        else:
            print("There is no one here to talk to.")
    
    elif command == "fight":
        inhabitant = current_room.get_character()
        if isinstance(inhabitant, Enemy):
            user_bag.show_items()
            combat_item = input("What will you fight with?: ").strip()
            if user_bag.has_item(combat_item):
                if inhabitant.fight(combat_item):
                    print(f"You have defeated {inhabitant.name}!")
                    current_room.set_character(None)  
                else:
                    print(f"{inhabitant.name} has defeated you. Better luck next time!")
                    break  
            else:
                print(f"You don't have a {combat_item} in your bag. {inhabitant.name} has defeated you. Better luck next time!")
                break
        else:
            print("There is no one here to fight with.")
    
    elif command == "i":
        user_bag.show_items()
    
    else:
        new_room = current_room.move(command)
        if new_room:
            current_room = new_room
            print("\n")
            current_room.get_details()
            inhabitant = current_room.get_character()
            if inhabitant is not None:
                inhabitant.describe()
                print("You can type 'talk' to interact with the character.")

