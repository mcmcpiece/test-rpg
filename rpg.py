#Text based game; only meant to exercise my programming skills in python
import rooms

current_room = "lobby"
inventory = []


def intro():
    print(f'''
Welcome, adventurer! You are in the {current_room}. Decide your move!
=====================================================================
Commands:
go [direction]
get [item]
check
use [object]
''')
    
def go(direction):
    global current_room
    if direction in rooms.rooms[current_room]["directions"]:
        if rooms.rooms[current_room]["directions"][direction] == "nothing":
            print("You can't go that way.")
            return
        else:
            current_room = rooms.rooms[current_room]["directions"][direction]
            print(f"You move to the {current_room}.")
    else:
        print("You can't go that way.")

def getitem(item):
    global inventory
    if item in rooms.rooms[current_room]["items"]:
        print(f"You pick up the {item}.")
        inventory.append(item)
        rooms.rooms[current_room]["items"].remove(item)
    else:
        print(f"There is no {item} here.")

def main():
    intro()
    while True:
        move = input(">").split(" ", 1)
        action = move[0]
        get_currentroom = rooms.rooms[current_room]
        if action == "go":
            direction = move[1]
            go(direction)
        elif action == "get":
            item = move[1]
            getitem(item)
        elif action == "check":
            print(f"You check your surroundings. {get_currentroom["description"]}")
        else:
            print("I did not quite understand that command. Please try again.")
            print('''
Commands:
go [direction]
get [item]
check
use [object]
''')

def list_items():
    for i in rooms.rooms:
        for item in rooms.rooms[i]["items"]:
            print(item)
            

list_items()

if __name__ == "__main__":
    try:
        main()
    except:
        print("\nDid you mean to exit? Exiting the game...")