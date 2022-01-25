"""Write a password generator in Python.
Be creative with how you generate passwords - strong passwords have a mix of lowercase letters,
uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your run-time code in a main method.
Extra:
1. Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""
import string
import random

#length = input("How long your password should be: ")

myDict = ["1", "2", "3", "4", "5"]
mySeparator = ""

z = mySeparator.join(myDict)

#print(z)


# string.digits[0:10])          random digit 0-9
# string.ascii_lowercase)       random lower letter a-z
# string.ascii_uppercase)       random upper letter A-Z
# string.printable[-38:-1])     random special character !@#

def create_password(length):
    password = []
    i = 1
    a = 0
    while i <= length:
        a = str(random_choice_of_base())
        print(f":draw by lot {random_choice_of_base()}")
        if a == "base1":

            password.append(random_digit())
        elif a == "base2":

            password.append(random_lower_letter())
        elif a == "base3":

            password.append(random_upper_letter())
        elif a == "base4":

            password.append(random_special_character())
        i += 1
    print(password)

def random_choice_of_base():
    base1 = random_digit()
    base2 = random_lower_letter()
    base3 = random_upper_letter()
    base4 = random_special_character()
    base = ["base1", "base2", "base3", "base4"]
    choice = random.choice(base)
    return choice


def random_digit():
    base = string.digits[0:10]
    x = random.choice(base)
    return x

def random_lower_letter():
    base = string.ascii_lowercase
    x = random.choice(base)
    return x

def random_upper_letter():
    base = string.ascii_uppercase
    x = random.choice(base)
    return x

def random_special_character():
    base = string.printable[-38:-1]
    x = random.choice(base)
    return x

create_password(5)
