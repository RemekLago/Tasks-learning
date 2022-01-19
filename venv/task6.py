"""Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)"""

user_word = input("Please write a word:")

polidrome_check = user_word[::-1]

if user_word == polidrome_check:
    print(f"your word is a polidrome")
else:
    print(f"your word is not a polidrome")

