import string
import os

print("Welcome to a game of Hang Man!")
print("Choose a game mode:")

gamemode = input("Default (start with this) or Freeplay\n")
gamemode.lower()

def hangman(userString):
    blankspaces = []
    lettersUsed = "Letters used: "
    gameStatus = True
    lives = 5
    for x in userString:
        if x in string.punctuation + " ":
            blankspaces.append(x)
        else:
            blankspaces.append("_")
    
    while gameStatus:
        print(" ".join(blankspaces))
        print("You have %d lives remaining" % lives)
        print(lettersUsed)
        guess = input("Please enter a letter or type in the whole word(s) to guess the whole thing\n")
        guess.lower()

        if guess == userString.lower():
            print("You got it!")
            gameStatus = False
        elif len(guess) == len(userString) and guess != userString.lower():
            print("You didn't get it! You can always try again.")
            lives -= 2
            
            if lives == 0:
                    gameStatus = False
                    print("You used all your lives! Game over!")
        elif len(guess) > 1:
            print("Please only enter one letter at a time")
        elif guess not in string.ascii_lowercase:
            print("You should be entering in a letter here")
        else:
            if guess not in userString.lower():
                lives -= 1
                lettersUsed += guess + ", "
                
                if lives == 0:
                    gameStatus = False
                    print("You used all your lives! Game over!")
            for x in range(len(userString)):
                if guess == userString[x].lower():
                    blankspaces[x] = userString[x]
            if "_" not in blankspaces:
                print(userString)
                print("You got it!")
                gameStatus = False

if gamemode == "default":
    hangman("Happy Birthday")
elif gamemode == "freeplay":
    word = input("Please enter your word(s): ")
    os.system("cls")
    hangman(word)