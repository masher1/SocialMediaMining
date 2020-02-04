"""
Assignment 1: Simple Python Program
Author: Malkiel Asher

Requirements:
* Create a Python module with a __main__ , and at least 100 lines of code. You should use: if  __name__  ==  "__main__":
* Define at least 1 class, and at least 1 function for each class you have defined. Your __main__ should instantiate objects of the classes you have designed, and use them to invoke the methods defined in those classes.
* Use list comprehensions to create lists.
* Use dictionary comprehensions to create dictionaries.
* Use at least 1 decision-making statement (if-elif)
* Use at least 1 looping statement (for or while).
* Use at least 1 try-except to catch some exceptions.
* Use the input() function, or command-line arguments, to get some user input
* Produce some, hopefully interesting, output
* Add comments to make your script easy to understand (not counted toward the 100 line requirement)
"""

import time
import WordBank
import random

# TODO: implement if statement for each letter that the user inputs and ignore the case of the letter
# TODO: impleement try catch for if the user inputs a non-number into the inputs where necessary

def main():
    print("Welcome to the Hangman Game!")
    print("Here is the hangman structure:")
    hangman()
    #time.sleep(3)
    genre = 0
    word = ""
    answer = []
    genre = int(input("What genre would you like to get a word from? (ENTER NUMBER)"
                  "\n1) Kitchen Utensils"
                  "\n2) Office Supplies"
                  "\n3) Popular Artists"
                  "\n4) Popular Actors"
                  "\n5) Popular Countries"
                  "\n6) RANDOM MODE\n\nChoice: "))
    if(genre != 6):
        word = WordBank.word_bank(genre);
    else:
        print("Entering rAnDoM MoDe!")
        rand_genre = (random.randint(1, 5))
        word = WordBank.word_bank(rand_genre)

    guess_the_letter(word)

#function made to have the player choose a letter that might be in the chosen word
def guess_the_letter(word):
    print("We have now chosen a word!"
          "\nLet's start the game!")
    wordLen = len(word)
    print("The word contains:", wordLen, "letters")
    print_(wordLen)
    #TODO: make sure only small case letters are acceptable  NO NUMBERS
    letter = input("\nWhat is your first letter choice?")
    WordBank.letCompare(letter, word)
    while (answer != word):
        letter = input("\nWhat is your next letter choice?")
        answer = WordBank.letCompare(letter, word)

def print_(wordLen):
    for x in range(wordLen):
        print(WordBank.color.UNDERLINE + ' ' + WordBank.color.END, end =" ")

# function made to draw the basic hangman base in ASCII
# TODO: make a switch statement to make a new hangman for each infraction from 1 to wordLen-1
def hangman(): # Makes the drawing for hangman
    print("___________")
    print("|         |")
    print("|         O")
    for x in range(4):
        print("|")
    print("‾‾")

#__name__ function to make sure client is starting from the correct module
def wrong_start():
    print("Please run first_module file")
if __name__  ==  "__main__":
    main()
else:
    wrong_start()