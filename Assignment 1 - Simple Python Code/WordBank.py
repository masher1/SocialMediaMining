import random

class font:
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

def letCompare(letter, word, answer, usedLetters, missed):
    count = 0;
    positions = []
    matched = False
    wordLetters = split(word)
    for i in range(len(word)):
        if(letter.lower() == wordLetters[i].lower()): #letter guessed matches one of the letters in the word
            count = count + 1;
            matched = True
            if(not(letter in usedLetters)):
                usedLetters.append(letter)
            positions.append(i)
    if (matched):
        print("letter \'",letter,"\' was matched", count, "times")
        print("You have used the following letter(s):", usedLetters)
        print("Position(s): ", positions)
    else:
        print("letter \'",letter,"\' is not in the word")
        first_module.hangman(1)
    for i in range(len(positions)):
        answer[positions[i]] = letter#answer.insert(positions[i], letter)
    print(answer)

    return (answer, usedLetters)

def split(word):
    return [char for char in word]

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
    # dict comprehension to create dict with words as keys and length of words as values
    wordLength = {f: len(f) for f in wordList}
    print("We are going to choose from the list of", genre, "which contains", numOfWords, "words!")

    #choose a random word
    rand_word = wordList[random.randint(1, numOfWords-1)]
    while(len(rand_word) < 7):
        rand_word = wordList[random.randint(1, numOfWords-1)]
    return rand_word