"""Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function."""
import random

new_list = []


def create_list(a, b):
    list1 = range(a, b)
    list2 = sorted(random.choices(list1, k=10))
    c = list2
    new_list.append(c[0])
    new_list.append(c[len(c) - 1])
    print(c)
    print(new_list)


def start(a, b):
    create_list(a, b)


start(5, 95)