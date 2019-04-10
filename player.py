# Room dictionaries.
room1 = {
    'name': 'North Corridor',
    'description': 'You see a diploma guarded by a homework assignment. '
                   'Maybe if you complete the homework you will get the grade'
                   '.',
    'items': ['diploma'],
    'exits': ['south']
}

room2 = {
    'name': 'South Campus',
    'description': 'You see a friendly looking old man. He gestures you to approach. You approach him. Maybe '
                   'you should talk to him.',
    'items': ['energy-shot'],
    'exits': ['north']
}

room3 = {
    'name': 'East Dorms',
    'description': 'It is very dark and you are having a hard time seeing.',
    'items': ['textbook'],
    'exits': ['west']
}

room4 = {
    'name': 'West hallway',
    'description': 'You walk into the hallway that used to be crowded with students.',
    'items': ['glasses'],
    'exits': ['east']
}

room5 = {
    'name': 'Study hall',
    'description': 'You see the empty table where you just cried yourself to sleep '
                   'and four doors leading out of the room....',
    'items': ['pencil'],
    'exits': ['north', 'south', 'east', 'west']
}

room6 = {'name': 'Dungeon',
         'description': 'You see an assessment test pulled up on the computer ready to take.',
         'items': ['passing-grade'],
         'exits': ['west']
}

# Player dictionary with basic stats, starting location, and inventory.
player = {
    'name': 'Cameron',
    'health': 100,
    'defense': 0,
    'attack': 5,
    'sleep': 40,
    'inventory': ['Study-guide', 'torch'],
    'equipped': ['backpack'],
    'location': room5
}

# Monster dictionaries.
monster = {'name': 'Homework Assignment',
           'health': 35,
           'attack': 20,
           'items': ['diploma'],
           'dialogue': 'You will never complete me and graduate!'
}

monster2 = {'name': 'Assessment test',
            'health': 40,
            'attack': 35,
            'items': ['passing-grade'],
            'dialogue': 'Weber States Bachelors Assessment cannot be passed!!'
}

# Character dictionary.
character = {
    'dialogue': 'How are you? My name is John. I lost my glasses years ago.'
                ' Please bring them back to me.',
    'dialogue2': 'Thank you for finding and returning my glasses to me! As a reward here is a key to the dungeon in '
                 'the East Dorms.'
}
