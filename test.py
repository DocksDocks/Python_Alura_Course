
def start():
    print("**********************************")
    print("   Welcome to the Hangman Game!   ")
    print("**********************************")


    secret_word = "Banana"
    hanged = False
    correct = False
    temp_word = '_'*len(secret_word)
    listTemp = list(temp_word)

    while not hanged and not correct:
        letter_guess = input("Guess a letter of the word: ")
        letter_guess = letter_guess.strip()
        
        for index,letter in enumerate(secret_word):
            if(letter_guess.lower() == letter.lower()):
                listTemp[index] = letter
                temp_word = ''.join(listTemp)
        print(temp_word)
        if(temp_word == secret_word):
            print("You won the game!")
            break
        
        
if (__name__ == "__main__"):
    start()