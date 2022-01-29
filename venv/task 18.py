"""Create a program that will play the “cows and bulls” game with the user. The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they have a “cow”.
For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess,
tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over.
Keep track of the number of guesses the user makes throughout teh game and tell the user at the end."""
import random

random_4digit = str(random.randint(1000, 9999))
user_number = str(1234)
cow = 0
bull = 0

def game(x,y):
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


def is_in_number(number_1_list,number_2_list):
    list2 = number_2_list
    list1 = number_1_list
    if list2[0] == list1[0]:
        cow += 1
    elif list2[0] == list[1] or list2[0] == list[2] or list2[0] == list[3]:
        bull += 1
    elif list2[1] == list1[1]:
        cow += 1
    elif list2[1] == list[0] or list2[1] == list[2] or list2[1] == list[3]:
        bull += 1
    elif list2[2] == list1[2]:
        cow += 1
    elif list2[2] == list[0] or list2[2] == list[1] or list2[2] == list[3]:
        bull += 1
    elif list2[3] == list1[3]:
        cow += 1
    elif list2[3] == list[0] or list2[3] == list[1] or list2[3] == list[2]:
        bull += 1
    print(cow)
    print(bull)

#game("1234", "4567")




