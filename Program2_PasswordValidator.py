#Steps:
# Create a program that check if password is valid
#The password is valid if all criteria are met:
#a. Greater than 15 letters
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char (!@#$%^&*()_+ etc)

password = input("Input your password:  ")
total_Characters = len(password)

last_char = password[total_Characters-1]
second_last = password[total_Characters-2]

password.islower()
casecheck = password.islower()


def first_Criteria (total_Characters):
    if total_Characters > 15:
        criteria1 = 1
    else:
        criteria1 = 0
        print ("Invalid.")
        print ("Password must have at least 15 characters!")
    return criteria1

def second_Criteria (casecheck):
    if casecheck is True:
            criteria2 = 0
            print ("Invalid")
            print ("Password must have at least one capital letter!")
    else:
        casecheck is False
        criteria2 = 1
    return  criteria2

    
first = first_Criteria (total_Characters)
second = second_Criteria (casecheck)




