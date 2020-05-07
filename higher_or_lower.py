from random import randrange

def guessing_game():
    user_guess = int(input("Enter a number between 0 an 10: "))
    while user_guess < 0 or user_guess > 10:
        user_guess = int(input("Invalid number. Enter a number between 0 an 10: "))
    comp_number = randrange(11)
    if user_guess > comp_number:
        print("Your guess was too high!")
    elif comp_number > user_guess:
        print("Your guess was too low!")
    else:
        print("Your guess was correct! Nice job!")
    print("The random number was " + str(comp_number) + ".")

guessing_game()