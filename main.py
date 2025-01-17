from room import Room

kitchen = Room("kitchen")
ballroom = Room("ballroom")
dininghall = Room("dining hall")

kitchen.set_description("A cold dark room with rats inside")

print(kitchen.get_description())



kitchen.describe()
