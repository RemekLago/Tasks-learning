"""Given a .txt file that has a list of a bunch of names, count how many of each name
there are in the file, and print out the results to the screen.
I have a .txt file for you, if you want to use it!"""

counter_lines = {}

with open("a.txt") as file:
    line = file.readline()
    while line:
        line = line.strip()
        if line in counter_lines:
            counter_lines[line] += 1
        else:
            counter_lines[line] = 1
        line = file.readline()
print(counter_lines)
