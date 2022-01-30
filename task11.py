"""Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below."""

user_number = int(input("Please enter your number: "))
list_of_divisors = [i for i in range(2, user_number) if user_number % i == 0]
# in range can't be 1 and the user number, we are looking for extra divisors

def is_prime_function (x):
    if len(list_of_divisors) == 0:
        print("Your number is a prime number")
    else:
        print("Your number is not a prime number")
        list_of_divisors.append(1)
        list_of_divisors.append(user_number)
        print(f"Divisions for your number {set(list_of_divisors)}")

is_prime_function(user_number)
