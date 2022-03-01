import json
import random

# Load the words from the word bank json file and return the array.
# Choose a random word in the dictionary.
def loadRandWord():
    with open('word-bank.json') as file:
        data = json.load(file)
    return random.choice(data)
        
# Change all the letters in the word to underscores and return that.
def hideWord(word):
    hiddenWord = ""
    for _ in word:
        hiddenWord += '_'
    return hiddenWord

# Process the letter in the word and show the correctly guessed letter on the hidden string.
def processCharInWord(letter, hiddenWord):
    pass


    # Top level code
    if __name__ == '__main__':
        user_input = 'Y'

        while user_input == 'Y':
            print('\nWelcome to the game of Hangman. You will have 4 lives to guess the correct word.')
            
            user_lives = 6

            guessed_so_far = list()
                
            actual_word = loadRandWord()

            hiddenWord = hideWord(actual_word)

            while user_lives != 0:

                # Ask user to guess a letter
                print(f'The hidden word: {hiddenWord}')
                user_guess = input('Please guess a letter in the word: ').upper().strip()
                
                # Register the letter and see if it's in the word
                if user_guess in actual_word or user_guess not in guessed_so_far:
                    processCharInWord(user_guess, hiddenWord) 
                elif user_guess in guessed_so_far:
                    print(f'You have alread guessed {user_guess}')
                else:
                    print(f'The letter {user_guess} is not in the word.')
                    user_lives -= 1
                    guessed_so_far.append(user_guess)
                # If it is, show the letters in the word and show the letter guessed so far.