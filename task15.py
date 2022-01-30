"""Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
"""

user_sentence = input("Please enter a short sentence: ")
rewerse_sentence = []

def rewerse():
    a = user_sentence.split(" ")
    b = len(a)
    for i in range(b):
        c = a[b-i-1]
        rewerse_sentence.append(c)
    print(rewerse_sentence)

rewerse()

#option2
def rewerse2():
    a1 = user_sentence.split(" ")
    a1.reverse()
    print(a1)

rewerse2()