"""Create a program that asks the user for a number and then
prints out a list of all the divisors of that number."""

number = int(input("Please enter your number: "))

list_of_divisors = range(1, number+1)
list_of_results = []

for i in list_of_divisors:
    if number % i == 0:
        list_of_results.append(i)
print(f"list of number divisors: {list_of_results}")


