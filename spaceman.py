# Set initial greating and input request from Player 1
word = input("Welcome to Spaceman: Hangman for the 21st century. \nTo begin, player 1 should please enter a word: ")

# Set intial arrays: the word that will be shown, the guesses, and the number of chances remaining
shownWord = []
pastGuesses = []
currentGuess = ""
lives = 7

# Hide the word from Player 2
def hide_word():
    global shownWord
    for char in word:
        shownWord.append("_")

# Request user input from Player 2
def get_character():
    global pastGuesses
    global currentGuess
    print("Enter your guess.")
    guess = input(">>>")
    currentGuess = guess
    pastGuesses.append(guess)



# Run through each letter in word. Adding method to remove lives in this function
# to take advantage of
# Working on!
def check_and_show_guess():
    global lives
    correctGuess = False
    for i, value in enumerate(word):
        if word[i] == currentGuess:
            shownWord[i] = currentGuess
            correctGuess = True
    if correctGuess == False:
        lives -= 1
    # return shownWord


# Function with all the methods to play game a turn
def play_turn():
    print(''.join(pastGuesses))
    print("Lives remaining: " + str(lives))
    print(''.join(shownWord))
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
