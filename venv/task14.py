"""Write a program (function!) that takes a list and returns a new list that contains all the elements
of the first list minus all the duplicates.

Extras:
1. Write two different functions to do this - one using a loop and constructing a list, and another using sets.
2. Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""

list1 = [a for a in range(1,100) if a % 2 == 0]
list2 = [a for a in range(1,100) if a % 4 == 0]
new_list = []


def list_no_duplicates(list1, list2):
    for i in list1:
        if i not in list2:
            new_list.append(i)
    print(new_list)

list_no_duplicates(list1, list2)

# extras1
list3 = set(list1 + list2)
print(list3)