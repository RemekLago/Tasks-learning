"""Write a password generator in Python.
Be creative with how you generate passwords - strong passwords have a mix of lowercase letters,
uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your run-time code in a main method.
Extra:
1. Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""
import string

#length = input("How long your password should be: ")

myDict = ["1", "2", "3", "4", "5"]
mySeparator = ""

x = mySeparator.join(myDict)

print(x)
# wybierz z jakiego rodzaju danych losujemy
# wybierz losowo cyfre 0-9
# wybierz losow litere a-z
# wybierz losowo znak specjalny

print(string.digits[0:10])
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.printable[-38:-1])