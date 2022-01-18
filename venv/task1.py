"""Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old."""

from datetime import date

user_name = input("Please enter your name: ").capitalize()
user_age = int(input("Please enter your age: "))
# I assume that user will not enter 0 or negative value
today = date.today()

# current year minus age of a user plus 100 years
year_user_age_100 = today.year - user_age + 100

print(f"Hello {user_name}, if you are a lucky man, you will turn 100 years old at {year_user_age_100}.")