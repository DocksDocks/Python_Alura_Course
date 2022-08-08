import random

def start():
    welcome_message()
    secret_word = load_secret_word()
    attempts = 7
    correct_letters = load_correct_letters(secret_word)
    hanged = False
    correct = False
    tried_letters = []
    while not hanged and not correct:
        letter_guess = ask_letter()
        if letter_guess in tried_letters:
            print('Careful! You already this letter.')
            continue
        if(letter_guess in secret_word):
            correct_letters = correct_letter_marker(secret_word,letter_guess,correct_letters)
        else:
            attempts -=1
            tried_letters.append(letter_guess)
            wrong_letter_message(attempts)
        print(f'Word: {correct_letters}')
        print(f'Letters not in the word: {tried_letters}')
        hanged = attempts < 1
        correct = correct_letters == secret_word
        if (hanged):
            lost_message(secret_word)
        if(correct):
            won_message()     

def wrong_letter_message(attempts):
    str = "You have {} attempts".format(attempts) if attempts > 1 else "You have {} attempt".format(attempts)
    print(f"Got it wrong!\n{str}")
    draw_hangman(attempts)

def correct_letter_marker(secret_word,letter_guess, correct_letters):
    listTemp = list(correct_letters)
    for index,letter in enumerate(secret_word):
        if(letter_guess == letter):
            listTemp[index] = letter
            correct_letters = ''.join(listTemp)
    return correct_letters
def ask_letter():
    letter_guess = input("\nGuess a letter of the word: ")[0]
    letter_guess = letter_guess.strip().upper()
    return letter_guess
        
def load_secret_word():
    file = open("words.txt", "r")
    words = []
    for line in file:
        line = line.strip().upper()
        words.append(line)
    file.close()
    number = random.randrange(0,len(words))
    secret_word = words[number]
    return secret_word

def load_correct_letters(secret_word):
    correct_letters = '_'*len(secret_word)
    return correct_letters
        
def welcome_message():
    print("**********************************")
    print("   Welcome to the Hangman Game!   ")
    print("**********************************")
    
def won_message():
    print("\n**********************************")
    print("Congratulations, you won the game!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print("**********************************\n")
    
def lost_message(secret_word):
    print("\n**********************************")
    print("Hanged! You lost the game.")
    print(f"The word was: {secret_word}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print("**********************************\n")
    
def draw_hangman(attempts):
    print("  _______     ")
    print(" |/      |    ")

    if(attempts == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(attempts == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(attempts == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(attempts == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(attempts == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(attempts == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (attempts == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
    
if (__name__ == "__main__"):
    start()