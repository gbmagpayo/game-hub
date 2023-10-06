# Game Hub

## Hangman Program flow
1. start
2. generate a random word
3. display: secretword, guessed letters, number of incorrect guessed left
4. ask user for an input
5. check if input is a letter guess or a word guess
    - if a letter guess
        1. check if it is already guessed (prompt again if true)
        2. check if letter in secret word
            - if true: add letter in guessed letters
            - if false: add letter in guess letters, subtract 1 from number of incorrect guesses
    - if a word guess:
        1. check if word guess is equal to secretword
            - if true: end and display correct guess
            - if false: subtract 1 from number of incorrect guesses

note: the game ends if player consumed the number of incorrect guesses or if the player was able to guess the word


