import os
# Set initial greating and input request from Player 1
os.system("clear")


class Spaceman():
    def __init__(self):
        """Initialize this node with the given data."""
        self.word = str.upper(input(
            "Welcome to Spaceman: Hangman for the 21st century. \nTo begin, player 1 should please enter a word: "))
        self.lives = 7
        self.shownWord = []
        self.pastGuesses = []
        self.currentGuess = ""

    def hide_word(self):
        for char in self.word:
            self.shownWord.append("_")

    def get_character(self):
        waitingForValidGuess = True
        while waitingForValidGuess == True:
            print("Guess a valid letter.")
            guess = str.upper(input(">>>"))
            if guess.isalpha() and len(guess) == 1 and guess not in self.pastGuesses:
                self.currentGuess = guess
                self.pastGuesses.append(guess)
                waitingForValidGuess = False

    def check_and_show_guess(self):
        correctGuess = False
        for index, value in enumerate(self.word):
            if self.word[index] == self.currentGuess:
                self.shownWord[index] = self.currentGuess
                correctGuess = True
        if correctGuess == False:
            self.lives -= 1

    def play_turn(self):
        os.system('clear')
        # drawing.draw_spaceman(lives)
        print("Past guesses: " + ', '.join(self.pastGuesses))
        print("Lives remaining: " + str(self.lives))
        print(' '.join(self.shownWord))
        self.get_character()
        self.check_and_show_guess()
        # Compare guess with word
        # Print "correct"/"incorrect"
        # Print hangman


game = Spaceman()
# Running code - play until win or lose
game.hide_word()
game.running = True
while game.running:
    if "_" not in game.shownWord:
        game.running = False
        print ("Game over, you win. You are amazing!")
    elif game.lives == 0:
        game.running = False
        print("Game over, you lose.")
    else:
        game.play_turn()


# Test function
def test():
    hide_word()
    play_turn()
