"""Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that
are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:
1. Randomly generate two lists to test this
"""
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = []

for i in a:
    if i in b:
        result.append(i)

print(set(result))

# extras 1
list_c = range(1, 100)
list_d = range(1, 70)
c = random.choices(list_c, k=20)
d = random.choices(list_d, k=15)
result2 = [i for i in c if i in d]
print(set(result2))




