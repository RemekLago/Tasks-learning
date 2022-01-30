"""Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum
of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)"""

results = [0, 1, 1]

# solution for numbers bigger than 3 if number is lower than 3 that requires to create to write new loop with if
def fibonnaci_sequence():
    number = int(input("How many numbers you want to generate: "))
    x = 0
    for i in range(0, number-3):
        x = results[i+2] + results[i+2-1]
        results.append(x)
    print(results)

fibonnaci_sequence()