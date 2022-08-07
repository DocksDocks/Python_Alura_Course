

from re import A


def start():
    print("**********************************")
    print("   Welcome to the Hangman Game!   ")
    print("**********************************")


    secret_word = "banana"
    hanged = False
    correct = False
    temp_word = '_'*len(secret_word)

    while not hanged and not correct:
        letter_guess = input("Guess a letter of the word: ")
        
        for index,letter in enumerate(secret_word):
            if(letter_guess == letter):
                listTemp = list(temp_word)
                listTemp[index] = letter_guess
                temp_word = ''.join(listTemp)
        print(temp_word)
        if(temp_word == secret_word):
            print("You won the game!")
            break