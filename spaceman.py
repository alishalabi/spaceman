# Import miscellaneous operating system interfaces (os) - This will help format temrinal
import os

# Set introduction

# Set initial greating and input request from Player 1
word = input("Welcome to Spaceman: Hangman for the 21st century. \nTo begin, player 1 should please enter a word: ")

# Set intial arrays: the word that will be shown, the guesses, and the number of chances remaining
shownWord = ""
guesses = []
lives = 5

# Instructions for Player 2


# Request user input from Player 2
def get_character():
    global guesses
    print("Enter your guess.")
    guess = input(">>>")
    guesses.append(guess)


# Add code to show blank guesses and correct guesses
def showWord():
    global shownWord
    global lives
    for char in word:
        if char not in guesses:
            shownWord = shownWord + str("_")
            lives -= 1
        else:
            shownWord = shownWord + str(char)
        #
        # if char in guesses:
        #     shownWord = shownWord + str(char)
        # else:
        #     shownWord = shownWord + str("_")
        #     lives -= 1
    print(shownWord)

# def test():
#     showWord()
#     print(lives)
#
# test()

# # Enter running code
running = True
while running:
    if word == ''.join(shownWord):
        print("You have guessed the correct word! Player 2 wins. Game Over.")
        running = False
    elif lives == 0:
        print("Game over! Player 2 loses. Game Over")
        running = False
    else:
        get_character()
        showWord()




# def get_character():
#     global lives
#     while lives > 0:
#         input_item = user_input("Enter Guess:")
#         add_guess(input_item)
#         showWord()
#         print(''.join(guesses))


# def test():
#     get_character()
#
#
# test()



# Second attempt:
# # Set initial greating and input request from Player 1
# word = input("Welcome to Spaceman: Hangman for the 21st century. \nTo begin, player 1 should please enter a word: ")
#
# # Set intial arrays: the word that will be shown, the guesses, and the number of chances remaining
# shownWord = []
# pastGuesses = ["e","p","x"]
# currentGuess = "e"
# lives = 5
#
# # Hide the word from Player 2
# def hide_word():
#     global shownWord
#     for char in word:
#         shownWord.append("_")
#
# # Request user input from Player 2
# def get_character():
#     global pastGuesses
#     global currentGuess
#     print("Enter your guess.")
#     guess = input(">>>")
#     currentGuess = guess
#     pastGuesses.append(guess)
#
#
#
# # Run through each letter in word. If guess
# # Working on!
# def check_and_show_guess():
#     for i, value in enumerate(word):
#         if word[i] == currentGuess:
#             shownWord[i] = currentGuess
#     return shownWord
#
#
#
#     # index = 0
#     # global shownWord
#     # for letter in word:
#     #     if char in word:
#     #         shownWord[index] = char
#     #     else:
#     #         return shownWord
#
#
#
#
# # Instructions for Player 2
#
#
#
# # Function with all the methods to play game a turn
# def play_turn():
#     print(''.join(pastGuesses))
#     print("Lives remaining: " + str(lives))
#     print(''.join(shownWord))
#     get_character()
#     check_and_show_guess()
#     # Compare guess with word
#     # Print "correct"/"incorrect"
#     # Print hangman
#
# # Test function
# def test():
#     hide_word()
#     play_turn()
#     print(shownWord)
#
# test()
