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


# string.digits[0:10])          random digit 0-9
# string.ascii_lowercase)       random lower letter a-z
# string.ascii_uppercase)       random upper letter A-Z
# string.printable[-38:-1])     random special character !@#


def final_password():
    length = int(input("How long your password should be: "))
    temporary_password(length)
    separator = ""
    final_pass = separator.join(temporary_password(length))
    print(f"Proposition of your password is: {final_pass}")


def temporary_password(length):
    password = []
    for i in range(0, length):
        print(i)
        a = str(random_choice_of_base())
        if a == "base1":
            password.append(random_digit())
        elif a == "base2":
            password.append(random_lower_letter())
        elif a == "base3":
            password.append(random_upper_letter())
        elif a == "base4":
            password.append(random_special_character())
        i += 1
        print(i)                                          # only for test
        print(f"draw by lot: {random_choice_of_base()}")  # only for test
    return password

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

final_password()