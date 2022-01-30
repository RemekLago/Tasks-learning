"""Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
One file has a list of all prime numbers under 1000, and the other file has a list of happy numbers up to 1000."""

def filetolistofints(filename):
	list_to_return = []
	with open(filename) as f:
		line = f.readline()
		while line:
			list_to_return.append(int(line))
			line = f.readline()
	return list_to_return

primeslist = filetolistofints("primenumbers.txt")
happieslist = filetolistofints("happynumbers.txt")

overlaplist = [elem for elem in primeslist if elem in happieslist]
print(overlaplist)
# not finished