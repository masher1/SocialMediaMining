import random # importing "random" for random operations
import time # importing "time" for realistic operations

print("Welcome to the program!")
time.sleep(1);
"""This program was designed as a Guess the Number Game"""
"""You will attempt to guess the number that the computer is thinking of between the range of 1 and 100"""

for x in range(0, 10):
    print("hmmm")
    randomNum = random.randrange(1, 100)
    time.sleep(.5);
    print("I have now chosen a number!")
    print("Let's play!")
    usrNum = int(input("Enter the number you think it is, or press 0 to quit: "))
    print("You chose: ", usrNum)
    if 0 == usrNum:
        exit()
    usrAnswr = int(input("My number is higher than : "))
    print("You chose: ", usrAnswr)
    if 0 == usrNum:
        exit()
    #print(randomNum)