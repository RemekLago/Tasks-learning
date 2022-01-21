"""Write a function that takes an ordered list of numbers (a list where the elements are in order
from smallest to largest) and another number.
The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
Extras:
    Use binary search.
"""
list = [1, 3, 5, 9, 13, 15, 18, 23, 27, 30, 35, 42, 43, 50]
number = int(input("Enter your number to check: "))

# solution1
def find1(number):
    for i in list:
        if i == number:
            return True
            break
        else:
            return False

if find1(number) == True:
    print("Is in list")
else:
    print("Is not in list")

find1(number)