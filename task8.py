"""Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner, and ask if the players want to start a new game)"""
import random

print("1 - rock \n2 - paper \n3 - scissors")
user = int(input("please choose one of options: "))
list = [1,2,3]
computer = random.choice(list)


def game(answer1, answer2):

        if user == computer:
            return ("It is a tie")
        elif user == 1:
            if computer == 2:
                return ("Computer wins")
            else:
                return ("User wins")
        elif user == 2:
            if computer == 1:
                return ("Computer wins")
            else:
                return ("User wins")
        elif user == 3:
            if computer == 1:
                return ("Computer wins")
            else:
                return ("User wins")
        else:
            return("Error, please check right option 1,2 or 3, try again")
        i += 1
print(game(user, computer))
