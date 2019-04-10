# TODO: Import Random
import random

# TODO: Create a list that contains 15 python keywords as strings
keywords = ['import', 'is', 'def', 'while', 'True', 'False', 'global',
            'finally', 'continue', 'break', 'try', 'except', 'elif',
            'else', 'if']


# TODO: Define a function called `create_list` that takes a string and returns a list that contains an underscore for each letter of the word.
# For example if your word was slice then create a list that contained five underscores: ['_', '_', '_', '_', '_']. Hint use len() and append().
def create_list(string):
    a_list = list('_' * len(string))
    return a_list


# TODO: Create a function called `progress` that takes two lists (list_a, list_b) and the current guess as a string. The function should contain a `for` loop that enumerates `list_a` and if the current guess is in `list_a` add it to `list_b`. This function creates a list after a letter has been guessed correctly.
# For example if the letter guessed is `s` and the word was `string` then it would return a list like this ['s', '_', '_', '_', '_']
def progress(list_a, list_b, guess):
    count = 0
    for item in list_a:
        if item == guess:
            list_b[count] = item
        count += 1
    return list_b


# TODO: Create a variable called `word` that select a random word from the list of words.
# TODO: Create a variable called `progress_list` and assign it what is returned from `create_list(word)`.
# TODO: Create a variable called `output` and assign it a string value that is not in your list of words.
# TODO: Create a variable called `lives` and assign the value of 10.
def game():
    word = keywords[random.randint(0, 14)]
    progress_list = create_list(word)

    output = ''

    lives = 10

    # TODO: Create a `while` loop that loops while `output` is not equal to `word`.

    # TODO in While: Check is `progress_list` is equal to the `word` as a list.
    # TODO: Set `output` equal to `word`
    # TODO: Print that they have won and break out of the while loop.
    print('Hangman! you have 10 lives. Incorrect guesses lose a turn.')
    print('Lives: ' + str(lives))
    print('Word: ' + ' '.join(progress_list))

    while output != word:
        if progress_list == word:
            output = word
            print("you won!")
            break

        else:
            guess = input("type your guess: ")
            guess = guess.lower()
        # TODO in While: Check is `guess` is equal to `word`.
        # TODO: Set `output` equal to `word`
        # TODO: Print that they have won and break out of the while loop.
        while guess == word:
            output = word
            print("you won!")
            break
        # TODO in While: Else Check if `guess` is greater than 1 and `guess` does not equal `word or that guess is a digit or that guess is less than 1.
        # TODO: Print that they have to guess one letter at a time.
        # TODO: Subtract 1 from `lives`

        if len(guess) > 1 and not word or guess.isdigit() or len(guess) < 1:
            print('guess one letter at a time')
            lives -= 1

        elif len(guess) == 1:
            if guess in word:
                print(guess + ' is in the word: ' + ' '.join(progress(word, progress_list, guess)))
                # TODO in While: Else Check if `lives` is equal to 0.
                # TODO: Print that they have run out of lives and break out of the while loop.
                # TODO in While: Else
                # TODO: Set a variable `guess` equal to an input with a prompt that contains the current number of lives
                #  and the current value of `progess_list`
                # TODO in While: Else Check if the length of `guess` is equal to 1
                # TODO: Check if `guess` is in `word` if it is print the return value of `progress` sending in the current word, the progress list and the players guess.
                # TODO: Else
                # TODO: Print something that tells the player they weren't correct and Subtract 1 from `lives`.
            else:
                lives -= 1
                print(guess + ' is not fond in the word. Lives left: ' + str(lives))

            if lives <= 0:
                print(" you ran out of lives")
                break
    play_again = input('do you want to play again? (Y/N): ')
    if play_again.upper() == "Y":
        print(' ')
        game()
    else:
        print('thanks for playing')


# TODO Next Steps (Required): Figure out how to ask if the player wants to continue.

# TODO Extra Credit: Print a hangman's noose

game()
