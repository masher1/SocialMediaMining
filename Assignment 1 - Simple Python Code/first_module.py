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

# TODO: implement if statement for each letter that the user inputs
# TODO: implement try catch for if the user inputs a non-number into the inputs where necessary

def main():
    print("Welcome to the Hangman Game!")
    print("Here is the hangman structure:")
    hangman()
    #time.sleep(3)
    genre = 0
    word = ""
    ready = False
    while (not ready):
        try:
            genre = int(input("What genre would you like to get a word from? (ENTER NUMBER)"
                              "\n1) Kitchen Utensils"
                              "\n2) Office Supplies"
                              "\n3) Popular Artists"
                              "\n4) Popular Actors"
                              "\n5) Popular Countries"
                              "\n6) RANDOM MODE\n\nChoice: "))
            if (genre < 6 and genre > 0):
                word = WordBank.word_bank(genre);
            elif (genre == 6):
                print("Entering rAnDoM MoDe!")
                rand_genre = (random.randint(1, 5))
                word = WordBank.word_bank(rand_genre)
            else:
                raise Exception()
            ready = True
        except:
            print(WordBank.font.RED + "ERROR: Please enter a number between 1 and 6" + WordBank.font.END)

    word = word.lower()
    guess_the_letter(word)

#function made to have the player choose a letter that might be in the chosen word
def guess_the_letter(word):
    print("We have now chosen a word!"
          "\nLet's start the game!")
    wordLen = len(word)
    wordChars = WordBank.split(word)
    answer = []
    # for i in range(wordLen-1):
    #     answer.insert(i,'_')
    answer = ['_' for w in range(wordLen)]
    #print("The default answer is:", answer) #for debugging purposes
    newWord = ""
    usedLetters = []
    spacePositions = []
    num = 0;
    print("The word contains:", wordLen, "letters")
    print_(wordLen)

    for i in range(wordLen):
        if(" " in wordChars[i]):
            num = num + 1;
            spacePositions.append(i)

    for i in range(num):
        answer[spacePositions[i]] = ' '
    #print("\nThere were", num, "spaces in", word) #for debugging purposes ONLY

    #REVIEWED: make sure only small case letters are acceptable  NO NUMBERS
    ready = False
    while (not ready):
        try:
            letter = input("What is your first letter choice?")
            if letter.isalpha() and letter.islower():
                ready = True
            else:
                raise Exception()
        except:
            print(WordBank.font.RED + "ERROR: Please enter lowercase, single character letters only" + WordBank.font.END)
    WordBank.letCompare(letter, word, answer, usedLetters)
    # TODO: implement the hangman structure somewhere here and limit it to 7 wrong guesses
    while (newWord != word):
        ready = False
        while (not ready):
            try:
                letter = input("What is your first letter choice?")
                if letter.isalpha() and letter.islower():
                    ready = True
                else:
                    raise Exception()
            except:
                print(
                    WordBank.font.RED + "ERROR: Please enter lowercase, single character letters only" + WordBank.font.END)
        (answer, usedLetters) = WordBank.letCompare(letter, word, answer, usedLetters)
        newWord = ""
        for x in answer:
            newWord += x
        print("Your Word so far:", newWord)
    #TODO: make a decision here to display congrats if the word was guessed correctly or if the game finished with a dead man
    print("Congratulations!")

def print_(wordLen):
    for x in range(wordLen):
        print(WordBank.font.UNDERLINE + ' ' + WordBank.font.END, end =" ")
    print("\n")
# function made to draw the basic hangman base in ASCII
# TODO: make a switch statement to make a new hangman for each infraction from 1 to wordLen-1
def hangman(x): # Makes the drawing for finished hangman
    print(WordBank.font.BLUE + "  _______" + WordBank.font.END)
    print(WordBank.font.BLUE + " |/      |" + WordBank.font.END)
    print(WordBank.font.BLUE + " |     (*_*)" + WordBank.font.END)
    print(WordBank.font.BLUE + " |      \|/" + WordBank.font.END)
    print(WordBank.font.BLUE + " |       |" + WordBank.font.END)
    print(WordBank.font.BLUE + " |      / \\" + WordBank.font.END)
    print(WordBank.font.BLUE + " |" + WordBank.font.END)
    print(WordBank.font.BLUE + "_|___" + WordBank.font.END)


def hangman(): # Makes the drawing for hangman
    print(WordBank.font.BLUE + "  _______" + WordBank.font.END)
    print(WordBank.font.BLUE + " |/      |" + WordBank.font.END)
    print(WordBank.font.BLUE + " |       O" + WordBank.font.END)
    print(WordBank.font.BLUE + " |" + WordBank.font.END)
    print(WordBank.font.BLUE + " |" + WordBank.font.END)
    print(WordBank.font.BLUE + " |" + WordBank.font.END)
    print(WordBank.font.BLUE + " |" + WordBank.font.END)
    print(WordBank.font.BLUE + "_|___" + WordBank.font.END)

#__name__ function to make sure client is starting from the correct module
def wrong_start():
    print("Please run first_module file")
if __name__  ==  "__main__":
    main()
else:
    wrong_start()