import random

class color:
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

def letCompare(letter, word):
    count = 0;
    positions = []
    answer = []
    usedLetters = []
    wordLetters = split(word)
    for i in range(len(word)):
        if(letter == wordLetters[i]): #letter guessed matches one of the letters in the word
            count = count + 1;
            if(not(letter in usedLetters)):
                usedLetters.append(letter)
            positions.append(i)
    print("letter \'",letter,"\' was matched", count, "times")

    print("You have used the following letters:", usedLetters)
    print("Positions: ", positions)

    for i in range(len(positions) - 1):
        answer.insert(positions[i], usedLetters[0])
        print(answer.insert(positions[i], usedLetters[0]))


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
    rand_word = wordList[random.randint(1, numOfWords)]
    return rand_word