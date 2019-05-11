# spaceman

## Requirements
If the guessed letter is in the mystery word, the position(s) of the letter(s) are revealed in the placeholders.
If a guessed letter occurs more than once in the word all the places that letter occurs are revealed.
If a player guesses all the letters in the word, they win the game.
For each incorrect guess a part of the Spaceman (a 7 part drawing of a Spaceman) is drawn.
If all 7 parts of the Spaceman are drawn then the player loses the game.

## Pseudo-code:
- Get word from Player 1 input
- Hide word behind behind underscores and print word
- Get guess from Player 2
- Store guess in array of guesses
- Run through each letter of word, if the guess matches a letter in the word then reveal that word (change the hidden word array, as well). If the word does not contain that guess, subtract one life
- If hidden word contains no underscores, players wins game
- If lives == 0, game over
- If lives > 0 and game is not over, play another turn

## Refactor Plan:
- Review duplicate code?
- Implementing a Spaceman class, converting functions to class methods
- Modify naming to improve semantics
