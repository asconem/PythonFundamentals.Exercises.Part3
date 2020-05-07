def get_user_guess():
    user_guess = int(input("Enter a number between 0 an 10: "))
    while user_guess < 0 or user_guess > 10:
        user_guess = int(input("Invalid number. Enter a number between 0 an 10: "))
    return user_guess

def get_random_number():
    from random import randrange
    return randrange(1,11)

def evaluate_result():
    user = get_user_guess()
    computer = get_random_number()
    if user > computer:
        print("Your guess was too high!")
    elif computer > user:
        print("Your guess was too low!")
    else:
        print("Your guess was correct! Nice job!")
    print("The random number was " + str(computer) + ".")

evaluate_result()