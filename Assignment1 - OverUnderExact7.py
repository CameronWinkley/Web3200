import random


# Set a variable called in_game to `True`
in_game = "True"


# Set a variable called `cash` to `150`
cash = 150


# Loop while `in_game` is true
while (in_game == "True"):

    # Set a variable called `die_one` to `random.randint(1, 6)`
    die_one = random.randint(1,6)
    # Set a variable called `die_two` to `random.randint(1, 6)`
    die_two = random.randint(1,6)
    # Set a variable called `roll` to `die_one` plus `die_two`
    roll = die_one + die_two
    bet_type = input("Will you bet exact, over, or under?\n").upper()
    bid = float(input("How much will you bid?\n"))

    # Subtract `bid` from cash and assign the new value back to `cash`
    print(cash)
    cash -= bid
    print(cash)
    # Create a set of if statements that check for the following:

    # `bet_type` is `EXACT` and `roll` is 7
    # Multiple bid by 4 and add it to `cash`
    if bet_type == "EXACT" and roll == 7:
        print(cash)
        print(" ")
        print(roll)
        cash += bid * 4
        print(cash)
        #print("You currently have" + cash)
    # `bet_type` is `OVER` and `roll` is greater than 7
    # Multiple bid by 2 add that to `cash`, print `cash`
    if bet_type == "OVER" and roll > 7:
        print(cash)
        print(roll)
        cash  += bid * 2
        print(cash)
    #print('You currently have' + cash)
    # `bet_type` is `UNDER` and `roll` is less than 7
    # Multiple bid by 2 add that to `cash`, print `cash`

    if bet_type == "UNDER" and roll < 7:
        print(cash)
        print(roll)
        cash += bid *2
        print(cash)
    # `Anything else should print `cash`

print(cash)

response = input('Play again? (Y/N)\n').upper()

# If response is 'Y' set `in_game` to True else set it to `False`
if response == "Y":
    in_game = "True"
else:
      if response == "N":
            in_game = "False"
print('Thanks for playing! Goodbye.')