import random
gameon = True

while gameon == True:
    print('''--- MasterMind---
    Guess the secret color code in as few tries as possible.
    Please, enter your color code.''')
# TODO: Create a list called `colors` with the values:  "R", "G", "B", "Y", "W", "P"
    colors = ['R', 'G', 'B', 'Y', 'W', 'P']
# TODO: Create a variable called `attempts` and assign it the value `0`
    attempts = 0
    # TODO: Create a variable called `game` and assign it the value `True`
    game = True
    # TODO: Create a variable called `color_code` and assign it a random sampling of 4 values from the `colors` list.
    color_code = random.sample(colors,4)
    print(color_code)
    # TODO: Create a an infinite loop using the variable `game`
    while game == True:
        # TODO: In the loop create a variable called `correct_color` with a value of `''`
        correct_color = ""
        # TODO: In the loop create a variable called `guessed_color` with a value of `''`
        guessed_color = ""
        # TODO: Get a guess from the user and store it in a variable called `player_guess` uppercase their guess.
        player_guess = input().upper()
        # TODO: Add 1 to `attempts`
        attempts += 1
        # TODO: Check if `color_code` is not equal to `'****'`
        if len(player_guess) != len(color_code):
            print('''the secret code should have four colors only.
            Try again''')
            continue
        # TODO: Create a for loop that loops 4 times
        # TODO: Check if the players guess is equal to the color code

        for i in range(4):
            if player_guess[i] not in colors:
                print('''use one of the following colors: R G B Y W P''')
                continue
        # TODO: add `*` to `correct_color`
        # TODO: Else if the players guess is not equal to the color code and the players guess is in color code
        # TODO: add `~` to `correct_color`
        # TODO: Else
        if correct_color != "****":
            for i in range(4):
                if player_guess[i] == color_code[i]:
                    correct_color += "#"
                if player_guess[i] != color_code[i] and player_guess[i] in color_code:
                    guessed_color += "~"
            print(len(correct_color), "Correct", " and", len(guessed_color), "of the correct color in wrong spots")
        # TODO: Check if `correct_color` is equal to `'****'`
        # TODO: Test if `attempt` is equal to 1 if it is then print a message saying great job you guessed it in one attempt. Else print a message about the number of attempts.
        # TODO: Set game to `False`
        if correct_color == "****":
            if attempts == 1:
                print("Great job! you guessed it first try!")
                game = False
                gameon = False
            else:

                print("Congrats! you got it! you needed " + str(attempts) + " attempts to get it correct")
                game = False
                gameon = False

        if correct_color != "****":
            print("please guess again: ")

            if attempts >= 1 and attempts < 6 and correct_color != "****":
                print("Next attempt: ")

            elif attempts >= 6:
                print("you lose! The secret color code was: " + str(color_code))
                game = False

    # TODO: While `game` is `False` ask the user if they want to play again if they do not want to play, exit the game.

    # TODO: If they want to play again set game to True and generate and new code
    while gameon == False:
            while game == False:
                finish_game = input("\nDo you want to play again (Y/N)?").upper()
                attempts = 0
                if finish_game == "Y":
                    game = True
                    gameon = True

                    continue
                elif finish_game == "N":
                    print("thanks for playing!")
                    exit(0)





