#Steps:
#Step 1: Create a program that ask for a sentence as input.
#Step 2: Display the number of words, vowels and consonants in the input 


sentence = input ("Type your sentence:  ")

number_Vowels = 0


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
    return number_Vowels


words = get_Words (sentence)
vowels = get_Vowels (sentence, number_Vowels)

print (f"Number of words:{words}")
print (f"Number of vowels: {vowels}")
