import random

def start():
    print("**********************************")
    print("   Welcome to the Hangman Game!   ")
    print("**********************************")

    file = open("words.txt", "r")
    words = []
    for line in file:
        line = line.strip().upper()
        words.append(line)
    file.close()
    number = random.randrange(0,len(words))
    secret_word = words[number]
    attempts = 7
    temp_word = '_'*len(secret_word)
    listTemp = list(temp_word)
    hanged = False
    correct = False
    tried_letters = []
    while not hanged and not correct:
        letter_guess = input("\nGuess a letter of the word: ")[0]
        letter_guess = letter_guess.strip().upper()
        if letter_guess in tried_letters:
            print('Careful! You already this letter.')
            continue
        if(letter_guess in secret_word):
            for index,letter in enumerate(secret_word):
                if(letter_guess == letter):
                    listTemp[index] = letter
                    temp_word = ''.join(listTemp)
        else:
            attempts -=1
            tried_letters.append(letter_guess)
            str = "You have {} attempts".format(attempts) if attempts > 1 else "You have {} attempt".format(attempts)
            print(f"Got it wrong!\n{str}")
        print(f'Word: {temp_word}')
        print(f'Letters not in the word: {tried_letters}')
        hanged = attempts < 1
        correct = temp_word == secret_word
        if (hanged):
            print("\n**********************************")
            print("Hanged! You lost the game.")
            print(f"The word was: {secret_word}")
            print("**********************************\n")
        if(correct):
            print("\n**********************************")
            print("Congratulations, you won the game!")
            print("**********************************\n")
if (__name__ == "__main__"):
    start()