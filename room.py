class Room:

    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.link_room = {}

    def get_description (self):
        return self.description

def set_description (self, room_description):
    self.description = room_description

def describe(self):
    print(self.description)

def get_name(self):
    return self.name

def set_name(self, room_name):
    self.name = room_name

def link_room(self, room_to_link, direction):
    self.linked_room[direction] = room_to_link

