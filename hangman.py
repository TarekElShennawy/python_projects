#Hangman app made by Tarek ElShennawy
from random import *

dictionary = ['fiddle', 'orange', 'table', 'glitter', 'wire']
sessionWord = 'fiddle'
sessionWordList = list(sessionWord)
mysteryWordList = list("X" * len(sessionWord))
iteration = 0
searchVar = 0

print('Welcome to hangman! Guess a letter..')
while iteration < 9:
   
    for letter in range(len(sessionWordList)):
        guessedLetter = input()
        
        if guessedLetter == sessionWordList[letter]:
            mysteryWordList[letter] = guessedLetter
           
            print('You guessed a letter right! You have ' + str(9 - iteration) + ' chances')
            mysteryWord = ''.join(mysteryWordList)
            print( 'The word is: ' + str(mysteryWord) )
        
            if mysteryWord == sessionWord:
                print('Congrats! you got the word!')
                exit()
        
        elif guessedLetter not in sessionWord:
            iteration += 1
            print('Nope! You have ' + str(9 - iteration) + ' chances')
            print( 'The word is: ' + str(mysteryWord) )
            
            mysteryWord = ''.join(mysteryWordList)
            if mysteryWord != sessionWord and iteration == 9:
                print('LOL losernerd!')
                exit()



