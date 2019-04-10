# TODO: Setup a dictionary with several key value pairs. It should contain an inventory list and the initial location. Call the dictionary `player`.
# TODO: Set up a dictionary of rooms each room having a description, a list of items and a dictionary of exits. Add 5 rooms.
from player import *

# TODO: From a text file read in the text introduction of your game and print it to the console.
story_file = open('./story.txt', 'r')
print(story_file.readline())
print(story_file.readline())
print(story_file.readline())
print('-----------------------------------------------------------------')
print('Please use all lowercase commands.')
print('Basic command examples: north, south, east, west, equip pencil, inventory, use torch, use energy-shot, '
      'cast graduate')
print('-----------------------------------------------------------------')


# TODO: Setup on infinite loop.
while True:

    # TODO: Create a variable and set it equal to the initial room stored in the `player` dictionary.

    # Allows player to input commands
    player_input = input('what is your choice? ')

    # TODO: Create a variable to store the command that is input by the user. Allow for commands like `take sword`
    #       **Hint: `split()` and store the different parts in their own variables.**
    command = player_input.split()

    # Check if a player can go a certain direction
    if 'north' in command or 'south' in command or 'east' in command or 'west' in command:
        if command[0] not in player['location']['exits']:
            print('Please choose a valid direction. type ''exits'' for help on where you can go')
        elif command[0] in player['location']['exits']:
            if player['location'] == room5:
                if command[0] == 'north':
                    player['location'] = room1
                    # print('Moved to room1')
                if command[0] == 'south':
                    player['location'] = room2
                    # print('Moved to room2')
                if command[0] == 'east':
                    player['location'] = room3
                    # print('Moved to room3')
                if command[0] == 'west':
                    player['location'] = room4
                    # print('Moved to room4')
            else:
                player['location'] = room5

            print(' ')
            print(player['location']['name'])
            print(player['location']['description'])

            if player['location'] == room4 and 'glasses' in player['location']['items']:
                print('You see a pair of glasses sitting on the ground.')
            elif player['location'] == room4:
                print('It looks like an empty place.')

    elif 'location' in command:
        print('Location: ' + str(player['location']['name']))

    elif 'exits' in command:
        print(player['location']['exits'])

    # TODO: One that allows the user to print the current inventory.
    elif 'inventory' in command:
        print('Current Inventory: ' + str(player['inventory']))

    elif 'items' in command:
        print(player['location']['items'])

    # TODO: One that allows the player to pick up single items and odd them to the inventory of the `player`.
    #       Also allow the user to add all items in the room to the inventory.
    elif 'take' in command:

        if command[1] in player['location']['items']:

            if command[1] == 'diploma':

                if monster['health'] <= 0:
                    player['location']['items'].remove(command[1])
                    player['inventory'].append(command[1])
                    print('You put the ' + str(command[1]) + ' in your inventory.')

                else:
                    print('You must defeat the monster to take that item.')

            else:
                player['location']['items'].remove(command[1])
                player['inventory'].append(command[1])
                print('You put the ' + str(command[1]) + ' in your inventory.')

                if command[1] == 'textbook':
                    print('Remember to open your book.')

                if command[1] == 'pencil':
                    print('Remember to sharpen your pencil.')

        elif command[1] not in player['location']['items']:
            print('That item does not exist in this room.')

        elif command[1] == 'all':
            player['inventory'] += player['location']['items']
            player['location']['items'].clear()
            print('You took all the items in the room.')

    # Use items in inventory.
    elif 'use' in command:
        # Checks if the item is in the player's inventory.
        if command[1] in player['inventory']:
            # Allows the player to use a torch.
            if command[1] == 'torch':
                # Checks if the player is in a location that needs a torch.
                if player['location'] == room3:

                    if 'textbook' in player['location']['items']:
                        print(
                            'You use the torch and you start to see around you. You notice a text book'
                            ' sitting on the ground in front of you.')
                    # If the textbook was picked up the player sees the door.
                    else:
                        print('You see a door and a key hole glowing.')

            if command[1] == 'energy-shot':
                # Increases players health.
                player['health'] += 50
                print('You used the ' + str(command[1]) + 'you gained 50 health and your health is now' + str(
                    player['health']) + '.')

                player['inventory'].remove(command[1])
                print('The now empty energy shot was removed from your inventory.')

            if command[1] == 'passing-grade':
                # Increases players sleep.
                player['health'] += 20
                print('You used the ' + str(command[1]) + 'you gained 20 minutes of sleep and your health is now' + str(
                    player['health']) + '.')

                player['inventory'].remove(command[1])

            # player instruction for their weapon.
            if command[1] == 'pencil':
                print('You can not use that item directly please use the equip command.')

            if command[1] == 'textbook':
                print('You can not use that item directly please use the equip command.')

            if command[1] == 'diploma':
                print('You look at the College Diploma and realize you are free. .')

            # Allows the player to use a key on the door.
            if command[1] == 'key':
                # Checks if the player is in the room with the door.
                if player['location'] == room3:
                    print(
                        'You use the key to unlock the door and walk into the darkness of the dungeon'
                        'with your torch lighting the way.')
                    # Change room to dungeon.
                    player['location'] = room6
                    print(' ')
                    print(player['location']['name'])
                    print(player['location']['description'])

        if command[1] in player['equipped']:

            if command[1] == 'pencil':
                print('You can not use that item directly please use the attack command.')

    elif 'cast' in command:

        if 'diploma' in player['inventory']:

            if command[1] == 'graduate' and player['sleep'] >= 10:
                print('you say "I am free!".')
                print('This cost you 10 minutes of sleep.')
                player['sleep'] -= 10

                if player['location'] == room6 and monster2['health'] != 0:
                    monster2['health'] -= 10
                    print('You did 10 damage to the monster!')
                    print(monster2['dialogue'])

                    if monster2['health'] <= 0:
                        monster2['health'] = 0
                        print('You killed the ' + str(monster['name']) + '!')
                        print('Your adventure is to be continued!')
                        print('If you want to explore the other areas type west otherwise type quit to exit.')

                    elif monster2['health'] > 0:
                        print('')
                        player['health'] -= 10
                        print('The Assessment test did 10 damage to you!')

            elif player['sleep'] < 10:
                print('You do not have enough sleep to think you''re free.')
            else:
                print('You do not know how to think you''re free.')
        else:
            print('You do not have a diploma.')

    elif player['health'] <= 0:
        print('You died!')
        print('Game Over...')
        break

    elif player['sleep'] <= 0:
        player['sleep'] = 0
        print('You ran out of freedom.')

    elif 'open' in command:
        if command[1] == 'door':
            if player['location'] == room3:

                if 'key' in player['inventory']:
                    print('Use the key to open  the door.')

                else:
                    print('The door is locked and will not open without the key.')
    # TODO: In one room add a monster and have the player fight the monster (add an attack verb). Store the monster stats in a dictionary.
    # TODO: In one room have the player talk with another character save the dialog in a dictionary.

    elif 'talk' in command:

        if player['location'] == room2:
            print(character['dialogue'])

            if 'glasses' in player['inventory']:

                if player['location'] == room2:
                    print(character['dialogue2'])
                    player['inventory'].remove('glasses')
                    player['inventory'].append('key')

            else:
                print('You do not have the glasses to give to John.')

        else:
            print('You can not give that item away.')

    elif 'attack' in command:

        if 'pencil' in player['inventory']:
            print('please equip the number 2 pencil to attack.')

        elif 'pencil' in player['equipped']:
            if player['location'] == room1:
                print('You attack the homework with purpose!')

                print(monster['dialogue'])
                monster['health'] -= player['attack']
                if monster['health'] <= 0:
                    monster['health'] = 0
                print('')
                print('You did ' + str(player['attack']) + ' damage to the homework assignment bringing it down to ' + str(
                    monster['health']) + ' health!')
                if monster['health'] == 0:
                    print('You passed the ' + str(monster2['name']) + '!')
                    monster['items'].remove('diploma')
                    print('You acquired a diploma from the ' + str(monster['name'] + '!'))
                    player['inventory'].append('diploma')

                if monster['health'] > 0:
                    player['health'] -= monster['attack']
                    print('The assignment did ' + str(monster['attack']) + ' damage to you bringing you down to ' + str(
                        player['health']) + ' health!')

            if player['location'] == room6:
                print('The assessment test seems to be immune to physical attacks! Maybe try declaring your freedom?')

        else:
            print('You need a number 2 Pencil to attack the Homework!')

    elif 'equip' in command:

        if command[1] in player['inventory']:
            player['inventory'].remove(command[1])
            player['equipped'].append(command[1])
            print('You equipped the ' + str(command[1]))

            if command[1] == 'pencil':
                player['attack'] += 15
                print('Your attack power is now ' + str(player['attack']))

            elif command[1] == 'textbook':
                player['defense'] += 5
                print('Your defense power is now ' + str(player['defense']))

        else:
            print('That item is not in your inventory.')

    elif 'equipped' in command:
        print(player['equipped'])

    elif 'name' in command:
        player['name'] = command[1]
        print('You changed your name to: ' + str(command[1]))

    elif 'stats' in command:
        print('')
        print('Name: ' + str(player['name']))
        print('Health: ' + str(player['health']))
        print('Attack Power: ' + str(player['attack']))
        print('Defense Power: ' + str(player['defense']))
        print('sleep: ' + str(player['sleep']))
        print('')
    # TODO: One that allows the user to quit.
    elif 'quit' in command:
        print('Thanks for playing!')
        break
    else:
        print('That is not a valid command.')

# Extra Credit:
# Create a map verb that prints a map of the dungeon. +5
# Allow rooms to be locked and only open with a key. +5
# Allow rooms to contain items that have their own verbs. For example a staff that can cast spells. +5
# Any other modification or verbs. +5

# Closes the accessed story file.
story_file.close()
