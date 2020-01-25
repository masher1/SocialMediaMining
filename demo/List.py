import random
""""This program was designed as a Guess the Number Game"""
"""You will think of a number and the computer will attempt to guess what that number is"""
"""This class is made for the list that of numbers out of which the number wil be chosen"""

listo = [None] * 100;

#print("List Before: ", listo);
for x in range(0, 100):
    listo[x] = x+1;
print("Generated List: ", listo); #print the list