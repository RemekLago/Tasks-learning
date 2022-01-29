"""Create a program that will play the “cows and bulls” game with the user. The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they have a “cow”.
For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess,
tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over.
Keep track of the number of guesses the user makes throughout teh game and tell the user at the end."""
import random

random_4digit = str(random.randint(1000, 9999))
user_number = str(1234)


"""
def game(x,y):
    split_numbers(x, y)
    is_in_number(x,y)

def split_numbers(number_1,number_2): # it works correctly
    number_1_list = []
    number_2_list = []
    for i in number_1:
        number_1_list.append(i)
    print(number_1_list) # for check
    for j in number_2:
        number_2_list.append(j)
    print(number_2_list) # for check
    return number_1_list, number_2_list

# nie wiem jak pobrać dane ze zwróconej tupli (number_1_list, number_2_list)
"""
#number_1_list = ['1', '2', '3', '4']
#number_2_list = ['6', '2', '3', '1']

def is_in_number(number_1_list,number_2_list):
    cow = 0
    bull = 0
    list2 = number_2_list
    list1 = number_1_list
    result = []
    for i in range(len(list2)):
        if list2[i] == list1[i]:
            cow += 1
            result.append(list2[i])
        elif list2[i] in list1:
            bull += 1
            result.append("X")
        else:
            result.append("X")
    print(f"You hit: {len(result)-result.count('X')} numbers are on the right place {result} and {bull} numbers are not at the correct place")
    print(f"cow = {cow}")
    print(f"bull = {bull}")
    extra_hits()

def extra_hits():
    x = input("Do you want to take another chance? Y/N...")
    if x == "Y" or x == "y":
        input("Please enter your number again")
        #...
    elif x == "N" or x == "n":
        print("Thank you for your game")
    else:
        print("Please write: Y or N")

is_in_number(['1', '2', '3', '4'], ['6', '2', '3', '1'])