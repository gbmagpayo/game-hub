import random

def generateRandomWord():
    ''' Generates a random word from a txt.file'''
    with open("words.txt", "r") as file:
        words = [word.strip() for word in file]
    return random.choice(words)

def getGuess(secretWord, guessedLetters):
    while True: 
        guess = input("Enter guess: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessedLetters:
                print("Letter is already guessed")
            else:
                return guess, False
    
        elif len(guess) == len(secretWord):
            return guess, True
        
        else:
            print("Invalid input")

def displayGame(secretWord, guessedLetters, numTriesLeft):
    print("Letters guessed:", ", ".join(guessedLetters))
    print(f"Tries left: {numTriesLeft}")
    for letter in secretWord:
        if letter in guessedLetters:
            print(letter, end = " ")
        else:
            print("_", end = " ")
    print()


def hangman():
    secretWord = generateRandomWord()

    guessedLetters= []
    numTriesLeft = len(secretWord) - 2

    #inside while true
    while True:
        if numTriesLeft == 0:
            print("Nice try")
            break

        if all(letter in guessedLetters for letter in secretWord):
            print("You guessed the word!")
            break

        displayGame(secretWord, guessedLetters, numTriesLeft)
        guess, isGuessWord = getGuess(secretWord, guessedLetters)

        if isGuessWord == True:
            if guess == secretWord:
                print("You guessed the word!")
                break
            else:
                print("Wrong Guess")
                numTriesLeft -= 1
        else:
            if guess in secretWord:
                guessedLetters.append(guess)
            else:
                guessedLetters.append(guess)
                numTriesLeft -= 1

def main():
    hangman()

if __name__ == "__main__":
    main()