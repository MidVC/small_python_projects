import random

# max lives possible
lives = 5

# secret words, which would be selected randomly
secret_words = ['pizza', 'ice cream', 'teeth', 'shirt', 'computer', 'plane']
word = random.choice(secret_words)

# clue, which shows the current guessing process
clue = []
length = len(word)
for index in range(length):
    if word[index] == ' ':
        clue.append(' ')
    else:
        clue.append('?')

# heart symbol, which is used to show the remaining lives
heart_symbol = u'\u2764'


# update_clue(letter, full_word, current_clue) returns true if the clue letter is in the full_word,
#   false otherwise
# requires: letter is a char letter from a to z,
#           full_word is a secret_word, and
#           current_clue is the clue list
# effects: may modify clue
def update_clue(letter, full_word, current_clue) -> bool:
    in_word = False
    for i in range(length):
        if letter == full_word[i]:
            in_word = True
            current_clue[i] = letter
    return in_word


# guess_word_correctly stores whether the word is guessed correctly
guess_word_correctly = False

# do the guesses
while lives > 0:
    # output the current status of the player
    print(clue)
    print('Lives remaining: ' + heart_symbol * lives)

    # ask for input until the input is a lower case letter
    guess = input('Please input the letter that you want to guess'
                  '(in lower case)')
    while not guess.islower():
        guess = input('Wrong input! Please input the letter that '
                      'you want to guess(in lower case)')

    # update the clue and lives, if needed, and output an appropriate message
    if update_clue(guess, word, clue):
        print(f'Good job! The letter {guess} is in the secret word!')
    else:
        print(f'The letter {guess} is not in the secret word!')
        print('You lost one life')
        lives = lives - 1

    # make a clue_string to determine whether the player have won the game
    clue_string = ''
    for c in clue:
        clue_string += c
    if clue_string == word:
        guess_word_correctly = True
        break

# Now all the guesses have been done, we would check whether the clue is equals
#   to the secret_word to determine if the player wins this game
if guess_word_correctly:
    print('You win this game! You successfully guessed the word ' + word)
else:
    print('You lost! The secret word is ' + word)
