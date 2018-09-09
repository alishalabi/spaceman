# word = "example"
# guesses = "e"
# lives = 7
#
# def play():
#     while lives > 0:
#         mistakes = 0
#         for letter in word:
#             if letter in guesses:
#                 print(letter)
#             else:
#                 print("_")
#                 mistakes += 1
#
# play()

word = "example"
wordLength = len(word)
guesses = "ea"
shownWord = ""
lives = 5

def showWord():
    global shownWord
    for char in word:
        if char in guesses:
            shownWord = shownWord + str(char)
        else:
            shownWord = shownWord + str("_")


# def printBlanks():
#     shownWord = ""
#     index = 1
#     while index <= wordLength:
#         if index == 1:
#             shownWord = shownWord + str("_")
#             index += 1
#         else:
#             shownWord = shownWord + str(" _")
#             index += 1


def test():
    print(word)
    print(wordLength)
    print(guesses)
    print(shownWord)
    showWord()
    print(shownWord)

test()
