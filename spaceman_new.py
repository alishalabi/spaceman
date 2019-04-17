import os
# Set initial greating and input request from Player 1
os.system("clear")


class Game:
    def __init__(self, word):
        """Initialize this node with the given data."""
        self.word = str.upper(input(
            "Welcome to Spaceman: Hangman for the 21st century. \nTo begin, player 1 should please enter a word: ")]
        self.lives = 7
        self.shownWord = []
        self.pastGuesses = []

    def hide_word():
        global shownWord
        for char in word:
            self.shownWord.append("_")


# Set intial arrays: the word that will be shown, the guesses, and the number of chances remaining
shownWord = []
pastGuesses = []
currentGuess = ""
lives = 7

# Hide the word from Player 2


# Request user input from Player 2
# Adding function to check if guess is valid here
# Adding function to make all guesses uppercase


def get_character():
    global pastGuesses
    global currentGuess
    waitingForValidGuess = True
    while waitingForValidGuess == True:
        print("Guess a valid letter.")
        guess = str.upper(input(">>>"))
        if guess.isalpha() and len(guess) == 1 and guess not in pastGuesses:
            currentGuess = guess
            pastGuesses.append(guess)
            waitingForValidGuess = False


# Run through each letter in word. Adding method to remove lives in this function
# to take advantage of
# Working on!
def check_and_show_guess():
    global lives
    correctGuess = False
    for index, value in enumerate(word):
        if word[index] == currentGuess:
            shownWord[index] = currentGuess
            correctGuess = True
    if correctGuess == False:
        lives -= 1
    # return shownWord


# Function with all the methods to play game a turn
def play_turn():
    os.system('clear')
    # drawing.draw_spaceman(lives)
    print("Past guesses: " + ', '.join(pastGuesses))
    print("Lives remaining: " + str(lives))
    print(' '.join(shownWord))
    get_character()
    check_and_show_guess()
    # Compare guess with word
    # Print "correct"/"incorrect"
    # Print hangman


# Running code - play until win or lose
hide_word()
running = True
while running:
    if "_" not in shownWord:
        running = False
        print ("Game over, you win. You are amazing!")
    elif lives == 0:
        running = False
        print("Game over, you lose.")
    else:
        play_turn()


# Test function
def test():
    hide_word()
    play_turn()
    # print(''.join(shownWord))
    # print(lives)
    # play_turn()
    # print(''.join(shownWord))
    # print(lives)
