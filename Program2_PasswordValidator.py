#Steps:
# Create a program that check if password is valid
#The password is valid if all criteria are met:
#a. Greater than 15 letters
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char (!@#$%^&*()_+ etc)


password = input("Input your password:  ")
total_Characters = len(password)
password.islower()
casecheck = password.islower()


def first_Criteria (total_Characters):
    if total_Characters > 15:
        criteria1 = 1
    else:
        criteria1 = 0
        print ("Invalid. Password must have more than 15 characters!")
    return criteria1

def second_Criteria (casecheck):
    if casecheck is True:
            criteria2 = 0
            print ("Invalid. Password must have at least one capital letter!")
    else:
        casecheck is False
        criteria2 = 1
    return  criteria2


def third_Criteria (password):
    for character in password:
        if character == "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
            criteria3 = 1
        else:
            print (f"Invalid. Password must have at least 1 number!")
            criteria3 = 0 
    return criteria3


import string

password_Set = set(password)
special_Characters_set = set(string.punctuation)


def fourth_Criteria ():
    if password_Set.intersection(special_Characters_set):
        criteria4 = 1
    else:
        criteria4 = 0
        print (f"Invalid password. There must be at least 1 special character.")
    return criteria4

     
first = first_Criteria (total_Characters)
second = second_Criteria (casecheck)
third = third_Criteria (password)
fourth = fourth_Criteria ()


if first + second + third + fourth == 4:
    print (f"Valid Password")




    




