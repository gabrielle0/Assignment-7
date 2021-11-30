#Steps:
#Step 1: Create a program that ask for a sentence as input.
#Step 2: Display the number of words, vowels and consonants in the input 

sentence = input ("Type your sentence:  ")

number_Vowels = 0
number_Consonants = 0
number_Spaces = 0

def get_Words (sentence, number_Spaces):
    number_Words  = 1
    for character in sentence:
        if character == " ":
            number_Words = number_Words + 1 
            number_Spaces += 1     
    return number_Words, number_Spaces


import string
special_Characters_set = set(string.punctuation)
sentence_Set = set(sentence)


def get_Vowels_consonants (sentence, number_Vowels, number_Consonants):
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
        else:
            if character.isdigit() or character in sentence_Set.intersection(special_Characters_set):
                number_Consonants += 0
            else:
                number_Consonants += 1             
    return number_Vowels, number_Consonants


words, spaces = get_Words (sentence, number_Spaces)
vowels, consonants = get_Vowels_consonants (sentence, number_Vowels, number_Consonants)

print (f"Number of words:{words}")
print (f"Number of vowels: {vowels}")
print (f"Number of consonants: {consonants - spaces} ")
