#Steps:
# Create a program that checks if password is valid
#The password is valid if all criteria are met:
#a. Greater than 15 letters
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char (!@#$%^&*()_+ etc)

import string

password = input("Input your password:  ")
total_Characters = len(password)
password.islower()
casecheck = password.islower()

password_Set = set(password)
special_Characters_set = set(string.punctuation)

numbers_List = "1234567890"
number_Set = set(numbers_List)

def first_Criteria (total_Characters):
    if total_Characters > 15:
        return True
    else:
        return False

def second_Criteria (casecheck):
    if casecheck is True:
        return False
    else:
        casecheck is False
    return  True

def third_Criteria ():
        if password_Set.intersection(number_Set):
            return True
        else:
            return False

def fourth_Criteria ():
    if password_Set.intersection(special_Characters_set):
        return True
    else:
        return False
        

def output (first, second, third, fourth):
    if first and second and third and fourth is True:
        print (f"Valid Password.")
    else:
        print (f"Invalid.")
        if first is False:
            print (f'Password must have more than 15 characters.')
        if second is False:
            print (f"Password must have at least 1 capital letter.")
        if third is False:
            print (f"Password must have at least 1 number.")
        if fourth is False:
            print (f"Password must have at least 1 special character.")


first = first_Criteria (total_Characters)
second = second_Criteria (casecheck)
third = third_Criteria ()
fourth = fourth_Criteria ()
output (first, second, third, fourth)



