#Steps:
#Step 1: Create a program that ask for a sentence as input.
#Step 2: Display the number of words, vowels and consonants in the input 


sentence = input ("Type your sentence:  ")

number_Vowels = 0
number_Consonants = 0

def get_Words (sentence):
    number_Words  = 1
    for character in sentence:
        if character == " ":
            number_Words = number_Words + 1
    return number_Words

def get_Vowels (sentence, number_Vowels):
    for character in sentence:
        if character == "a":
            number_Vowels += 1
        elif character == "e":
            number_Vowels += 1
        elif character == "i":
            number_Vowels += 1
        elif character == "o":
            number_Vowels += 1
        elif character == "u":
            number_Vowels += 1
    return number_Vowels

def get_Consonants (sentence, number_Consonants):
    for character in sentence:
        if character == "b":
            number_Consonants += 1
        elif character == "c":
            number_Consonants += 1
        elif character == "d":
            number_Consonants += 1
        elif character == "f":
            number_Consonants += 1
        elif character == "g":
            number_Consonants += 1
        elif character == "h":
            number_Consonants += 1
        elif character == "j":
            number_Consonants += 1
        elif character == "k":
            number_Consonants += 1
        elif character == "l":
            number_Consonants += 1
        elif character == "m":
            number_Consonants += 1
        elif character == "n":
            number_Consonants += 1
        elif character == "p":
            number_Consonants += 1
        elif character == "q":
            number_Consonants += 1
        elif character == "r":
            number_Consonants += 1
        elif character == "s":
            number_Consonants += 1
        elif character == "t":
            number_Consonants += 1
        elif character == "v":
            number_Consonants += 1
        elif character == "w":
            number_Consonants += 1
        elif character == "x":
            number_Consonants += 1
        elif character == "y":
            number_Consonants += 1
        elif character == "z":
            number_Consonants += 1
    return number_Consonants
            

words = get_Words (sentence)
vowels = get_Vowels (sentence, number_Vowels)
consonants = get_Consonants (sentence, number_Consonants)

print (f"Number of words:{words}")
print (f"Number of vowels: {vowels}")
print (f"Number of consonants: {consonants}")
