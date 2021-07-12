#Defining the variables used in the program
vowels = 0
consonants = 0
i = 0

#Ask the user for the number of lines
print("How many lines will there be?")
lines = input()

#Main loop to check if a letter is a vowel. If it isnt a vowel but is an alphabet letter then it is considered a consonant.
while i != int(lines):
    sent_value = input()
    list_sen = list(sent_value.lower())
    for letter in range(len(list_sen)):
        if list_sen[letter] == "e" or list_sen[letter] == "o" or list_sen[letter] == "a" or list_sen[letter] == "i" or list_sen[letter] == "u":
            vowels += 1
        elif list_sen[letter].isalpha():
            consonants += 1
        else:
            pass
    i += 1

#Print the total number of vowels and consonants
print("Number of vowels: " + str(vowels) + "\nNumber of consonants: " + str(consonants))
