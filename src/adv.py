from room import Room
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

# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
character_name = input("Choose your adveturers name:")
player = Player(character_name, room['outside'])
print(player)
direction = ""

while player.lives == True:
    # -----------------outside-------------------------

    if player.location == room['outside']:
        direction = input('choose a direction ( n q to quit ):')
        if direction == "n":
            player.location = room['foyer']
            print(player)
        if direction == "q":
            print(f"{player.char_name} leaves the adventure")
            player.lives = False

    # -----------------foyer-------------------------

    if player.location == room['foyer']:
        direction = input('choose a direction ( s n e or q to quit ):')
        if direction == "s":
            player.location = room['outside']
            print(player)
        if direction == "n":
            player.location = room['overlook']
            print(player)
        if direction == "e":
            player.location = room['narrow']
            print(player)
        if direction == "q":
            print(f"{player.char_name} leaves the adventure")
            player.lives = False

    # -----------------overlook-------------------------

    if player.location == room['overlook']:
        direction = input('choose a direction ( s or q to quit ):')
        if direction == "s":
            player.location = room['foyer']
            print(player)
        if direction == "q":
            print(f"{player.char_name} leaves the adventure")
            player.lives = False

    # -----------------narrow-------------------------

    if player.location == room['narrow']:
        direction = input('choose a direction ( w, n or q to quit ):')
        if direction == "w":
            player.location = room['foyer']
            print(player)
        if direction == "n":
            player.location = room['treasure']
            print(player)
        if direction == "q":
            print(f"{player.char_name} leaves the adventure")
            player.lives = False

    # -----------------treasure-------------------------

    if player.location == room['treasure']:
        direction = input('choose a direction ( s or q to quit ):')
        if direction == "s":
            player.location = room['narrow']
            print(player)
        if direction == "q":
            print(f"{player.char_name} leaves the adventure")
            player.lives = False

# while direction != "n" or direction != "q":
#     direction = input('choose a direction ( n, s, e, w or q to quit ):')
#     if direction == "n":
#         player.location = room['foyer']
#         print(player)fa
#     if direction == "q":
#         print(f"{player.char_name} leaves the adventure")


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# t
