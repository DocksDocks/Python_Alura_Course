import random

def start():
    print("**********************************")
    print("    Welcome to the Guess Game!    ")
    print("**********************************")

    secret_number = random.randrange(1,101)
    tries = 0
    points = 1000

    print("Which difficulty level would you like to play?")
    print("(1) Easy (2) Medium (3) Hard")

    while True:
        difficulty_level = int(input("Define the difficulty: "))
        if difficulty_level is 1 or difficulty_level is 2 or difficulty_level is 3:
            break

    if(difficulty_level == 1):
        tries = 20
    elif(difficulty_level == 2):
        tries = 10
    else:
        tries = 5

    for round in range(1, tries + 1):
        print("Try {} of {}".format(round, tries))

        guess_str = input("Guess a number between 1 and 100: ")
        print("You guessed: " , guess_str)
        guess = int(guess_str)

        if(guess < 1):
            print("This number is less than 1! You need to guess a number between 1 and 100!")
            continue
        elif(guess > 100):
            print("This number is greater than 100! You need to guess a number between 1 and 100!")

        correct = guess == secret_number
        greater = guess >  secret_number
        lesser  = guess <  secret_number

        if(correct):
            print("You got the correct answer and made {} points!".format(points))
            break
        else:
            if(greater):
                print("You missed it! You guessed a number greater than the secret number.")
            elif(lesser):
                print("You missed it! You guessed a number lesser than the secret number.")
            lost_points = abs(secret_number - guess)
            points = points - lost_points

    print("**********************************")
    print("      End of the Guess Game!      ")
    print("**********************************")


