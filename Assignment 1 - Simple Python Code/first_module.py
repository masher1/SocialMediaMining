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

def main():
    print("Welcome to the Hangman Game!")
    print("Here is the hangman structure:")
    hangman()
    time.sleep(3)
    genre = input("What genre would you like to get a word from? (ENTER NUMBER)"
                  "\n1) Kitchen Utensils"
                  "\n2) Office Supplies"
                  "\n3) Popular Artists"
                  "\n4) Popular Actors"
                  "\n5) Computer Parts"
                  "\n6) RANDOM MODE\n\nChoice:")



def hangman(): # Makes the drawing for hangman
    print("___________")
    print("|         |")
    print("|         O")
    for x in range(4):
        print("|")
    print("‾‾")




def wrong_start():
    print("Please run first_module file")

if  __name__  ==  "__main__":
    main()
else:
    wrong_start()