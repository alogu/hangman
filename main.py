import json
import random

# Load the words from the word bank json file and return the array.
def loadWords():
    with open('word-bank.json') as file:
        data = json.load(file)
    return data

# Select a random word to be chosen for 
def selectRandWord(words):
    pass


if __name__ == '__main__':
    pass