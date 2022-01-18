"""Ask the user for a number.
Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?"""

user_number = int(input("Write your number: "))

if user_number % 2 == 0:
    print(f"The number you put in ({user_number}) is even")
else:
    print(f"The number you put in ({user_number}) is odd")