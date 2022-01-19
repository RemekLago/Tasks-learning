"""Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:
1. Keep the game going until the user types “exit”
2. Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
import random

x = random.randint(1,9) #the number chosen by computer
y = 0                   #the number chosen by user
i = 0

while y != x:
    y = int(input("Enter your number, if you want to quit put 0.... :"))
    print(x) # only for check
    i += 1
    if y == 0:
        print("Thank you for game")
    elif y > x:
        print("To high")
    elif y < x:
        print("To low")
    else:
        print(f"You guess my number and you needed {i} trials")
        break












"""
import random
x = 0
y = random.randint(1, 9)
i = 0

while x != y and x != "exit":
    x = input("Try to ques my number (from 1 to 9) and write it here --> ")

    if x == "exit":
        break
    x = int(x)
    i += 1
    if x > y:
        print("sorry, to high, try again")
    elif x > y:
        print("sorry, to low, try again")
    else:
        print("You are lucky, you guessed my number")
        print("You need only", i, "tries")
input()
"""