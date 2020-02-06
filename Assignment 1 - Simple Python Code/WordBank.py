import random
import first_module

class font:#ASCII color codes
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#this method does most of the work of comparing the letters
def letCompare(letter, word, answer, usedLetters, missed):
    count = 0; #Count how many times a letter has been matched
    positions = []
    matched = False #The letters are the same
    ignore = False # vaariable to check if you should ignore the first case of correct letter showing up or not
    repeated = False  #The letter has been chosen before therefore is a repeated letter
    new_list = new_list = ['  _______', ' |/      |', '|', ' |', ' |', ' |', ' |', '_|___']
    wordLetters = split(word)# split each word into individual letters
    for i in range(len(word)):
        if(letter.lower() == wordLetters[i].lower()): #letter guessed matches one of the letters in the word
            count = count + 1
            matched = True #there was a match between the letter put in and one of the letters in the word
            positions.append(i)
            if (not (letter in usedLetters)):  # letter chosen by user is not in usedLetters
                ignore = True;
    if not ignore and matched:
        print(font.RED + "ERROR: You have already tried this letter and it worked" + font.END)
        repeated = True;
    elif (not matched and (letter in usedLetters)):
        print(font.RED + "ERROR: You have already tried this letter but it didn't work" + font.END)
        repeated = True;
    #if (not (letter in usedLetters)):
        #usedLetters.append(letter)
    if (not (letter in usedLetters)):  # letter chosen by user is not in usedLetters
        usedLetters.append(letter)
        ignore = True;
    if (matched and not repeated): #the letter is matched and it is the first time it appears
        print("letter \'",letter,"\' was matched", count, "times")
        print("You have used the following letter(s):", usedLetters)
        print("Position(s): ", positions)
    elif(not repeated):
        missed = missed + 1
        newWord = ""
        for x in answer:
            newWord += x
        print("letter \'",letter,"\' is not in the word")
        print("You have used the following letter(s):", usedLetters)
        done = first_module.HangDraw(missed, new_list) #this will let us know if the user has failed and therefore the program is done
        if done:
            print(font.RED + font.BOLD + "The word was:", word + font.END)
            print(font.RED + font.BOLD + "You guessed:", newWord + font.END)
            return 0, 0, 0

    #assign the new letter to the final user guessed answer
    for i in range(len(positions)):
        answer[positions[i]] = letter#answer.insert(positions[i], letter)
    return (answer, usedLetters, missed) #These are the variables we want to keep through the game.

#This function is used to split the word into individual characters
def split(word):
    return [char for char in word]

#the word_bank function will help determine which file to use
def word_bank(genre):#this method is designed to choose a word bank from a variety of files
    switcher = {
        1: 'Kitchen_Utensils',
        2: 'Office_Supplies',
        3: 'Popular_Artists',
        4: 'Popular_Actors',
        5: 'Popular_Countries',
        6: '',
    }
    genre = switcher.get(genre, "Wrong input!")
    #open file
    numOfWords = 0;
    file_name = genre +".txt"
    wordList = [word.rstrip('\n') for word in open(file_name)] #list comprehension to gather a list of all the words we could have
    numOfWords = len(wordList)
    print("We are going to choose from the list of", genre, "which contains", numOfWords, "words!")

    #choose a random word
    rand_word = wordList[random.randint(1, numOfWords-1)]
    while(len(rand_word) < 7):
        rand_word = wordList[random.randint(1, numOfWords-1)]
    return rand_word