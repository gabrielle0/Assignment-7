#Steps:
#Step 1: Create a program that ask for a sentence as input.
#Step 2: Display the number of words, vowels and consonants in the input 


sentence = input ("Type your sentence:  ")

def get_Words ():
    count_Spaces = 1
    for c in sentence:
        if c == " ":
            count1 = count_Spaces + 1
            number_Words = count1
    return number_Words


        

words = get_Words ()


print (f"Number of words:{words}")

