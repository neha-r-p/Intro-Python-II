# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def __str__(self):
        return f'{self.name} is currently in room {self.current_room}'
    
    def __repr__(self):
        return f'Player({repr(self.name)})'
    
    def add_item(self, item):
        for thing in self.current_room.items:
            if thing == item:
                self.items.append(item)
                self.current_room.items.remove(item)
                print(f"\nYou have picked up {item}\n")
                # print(self.current_room.items)
                # print("thing", thing)
                # print("self items", self.items)
            else:
                print(f"\nThe room does not have {item}.\n")
    
    def drop_item(self, item):
        for thing in self.items:
            if thing == item:
                self.items.remove(item)
                self.current_room.items.append(item)
                print(f"\nYou have dropped {item}.\n")