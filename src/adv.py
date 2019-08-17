from room import Room
from item import Item
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

item = {
    '1': Item("Lighted Torch", " A torch is found on the wall with a flame alit showing the room only leaving the far corners shadowed in darkness."),
    '2': Item("mana", "food as good as the day is new how it got there who knows."),
    '3': Item("gold", "a few coins abandoned at the behest of god knows what"),
    '4': Item("regents", "a collection of curious powders, roots and other odd unspeakables"),
    '5': Item("flask", "a firmented unknown fluid smells of an intoxicating odor as in aged whiskey"),
    '6': Item("note", "a blood smeared note written in haste it says 'THEYRE HERE MUST GET HELP!!'")
}


# Make a new player object that is currently in the 'outside' room.
character_name = input("Choose your adventurers name:")
player = Player(character_name, room['outside'])
print(player)
direction = ""

while player.lives == True:
    # -----------------outside-------------------------

    if player.location == room['outside']:
        Room.item = item['1']
        print(Room.item)
        item_collect = item['1'].name
        direction = input(
            'choose an option: \n press n to travel north\n press g to grab item in room\n press a to view character status and items carried\n press d to drop an item\n press q to quit\n:')
        if direction == "n":
            player.location = room['foyer']
            print(f"{player.char_name} has entered the {player.location}")

        if direction == "q":
            print(f"{player.char_name} leaves the adventure")
            player.lives = False
        if direction == "g":
            grab_item = input("Which item would thou like to grab?")
            if grab_item == item_collect:
                print(f"You have obtained the {item_collect}")
                player.item.append(item_collect)

        if direction == "a":
            print(f"Items:{player.item}")

        if direction == "d":
            drop_item = input("which item would you like to drop?")
            for it in player.item:
                if drop_item == it:
                    player.item.remove(it)
    # -----------------foyer-------------------------

    if player.location == room['foyer']:
        Room.item = item['2']
        item_collect = item['2'].name
        print(Room.item)
        direction = input('choose an option \n press s to travel south \n press n to travel north \n press e to travel east \n press g to grab item in room\n press a to view character status and items carried\n press d to drop an item\n press q to quit\n:')
        if direction == "s":
            player.location = room['outside']
            print(f"{player.char_name} has entered the {player.location}")
        if direction == "n":
            player.location = room['overlook']
            print(player)
        if direction == "e":
            player.location = room['narrow']
            print(f"{player.char_name} has entered the {player.location}")
        if direction == "q":
            print(f"{player.char_name} leaves the adventure")
            player.lives = False
        if direction == "g":
            grab_item = input("Which item would thou like to grab?")
            if grab_item == item_collect:
                print(f"You have obtained the {item_collect}")
                player.item.append(item_collect)
        if direction == "a":
            print(f"Items:{player.item}")
        if direction == "d":
            drop_item = input("which item would you like to drop?")
            for it in player.item:
                if drop_item == it:
                    player.item.remove(it)

    # -----------------overlook-------------------------

    if player.location == room['overlook']:
        Room.item = item['3']
        item_collect = item['3'].name
        print(Room.item)
        direction = input(
            'choose an option: \n press s to travel south\n press g to grab item in room\n press a to view character status and items carried\n q to quit:')
        if direction == "s":
            player.location = room['foyer']
            print(f"{player.char_name} has entered the {player.location}")
        if direction == "q":
            print(f"{player.char_name} leaves the adventure")
            player.lives = False
        if direction == "g":
            grab_item = input("Which item would thou like to grab?")
            if grab_item == item_collect:
                print(f"You have obtained the {item_collect}")
                player.item.append(item_collect)
        if direction == "a":
            print(f"Items:{player.item}")
        if direction == "d":
            drop_item = input("which item would you like to drop?")
            for it in player.item:
                if drop_item == it:
                    player.item.remove(it)

    # -----------------narrow-------------------------

    if player.location == room['narrow']:
        Room.item = item['4']
        item_collect = item['4'].name
        print(Room.item)
        direction = input(
            'choose an option: \n press w to travel west\n press n to travel north\n press g to grab item in room\n press a to view character status and items carried\n press d to drop an item\n press q to quit\n:')
        if direction == "w":
            player.location = room['foyer']
            print(f"{player.char_name} has entered the {player.location}")
        if direction == "n":
            player.location = room['treasure']
            print(f"{player.char_name} has entered the {player.location}")
        if direction == "q":
            print(f"{player.char_name} leaves the adventure")
            player.lives = False
        if direction == "g":
            grab_item = input("Which item would thou like to grab?")
            if grab_item == item_collect:
                print(f"You have obtained the {item_collect}")
                player.item.append(item_collect)
        if direction == "a":
            print(f"Items:{player.item}")
        if direction == "d":
            drop_item = input("which item would you like to drop?")
            for it in player.item:
                if drop_item == it:
                    player.item.remove(it)

    # -----------------treasure-------------------------

    if player.location == room['treasure']:
        Room.item = item['5']
        item_collect = item['5'].name
        print(Room.item)
        direction = input(
            'choose an option: \n press s to travel south\n press g to grab item in room\n press a to view character status and items carried\n press d to drop an item\n press q to quit\n:')
        if direction == "s":
            player.location = room['narrow']
            print(f"{player.char_name} has entered the {player.location}")
        if direction == "q":
            print(f"{player.char_name} leaves the adventure")
            player.lives = False
        if direction == "g":
            grab_item = input("Which item would thou like to grab?")
            if grab_item == item_collect:
                print(f"You have obtained the {item_collect}")
                player.item.append(item_collect)
        if direction == "a":
            print(f"Items:{player.item}")
        if direction == "d":
            drop_item = input("which item would you like to drop?")
            for it in player.item:
                if drop_item == it:
                    player.item.remove(it)
