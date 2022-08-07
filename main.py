import guess_game as gg
import hangman_game as hang

print("*********************************")
print("        Choose your game!        ")
print("*********************************")

print("(1) Hangman (2) Guess Game")

game = int(input("Which game would you like to play? "))

if (game == 1):
    print("Starting Hangman")
    hang.start()
elif (game == 2):
    print("Starting Guess Game")
    gg.start()