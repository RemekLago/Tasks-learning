"""Checking Tic Tac Toe results from a few examples
1 - player1 tokens
2 - player2 tokens
0 - empty, not filled"""


game_1 = [[1, 2, 0],
          [2, 1, 0],
          [2, 1, 1]]
#def game(game):


def checking_rows(game):
    score = None
    for i in range(3):
        for j in range(1):
            if game[i][j] == game[i][j+1] == game[i][j+2]:
                score = 1
            else:
                score = 0
        return score

def checking_columns(game):
    score = 0
    for j in range(3):
        for i in range(1):
            if game[i][j] == game[i+1][j] == game[i+2][j]:
                score = 1
            else:
                score = 0
            print(score)

def checking_diagonals(game):
    score = 0
    for i in range(1):
        for j in range(1):
            if game[i][j] == game[i+1][j+1] == game[i+2][j+2]:
                score = 1
            else:
                score = 0
            print(score)
    for i in range(1):
        for j in range(1):
            if game[i][j+2] == game[i+1][j+1] == game[i+2][j]:
                score = 1
            else:
                score = 0
            print(score)

checking_diagonals(game_1)

#Other solution
"""
def checkGrid(game):
	# rows
	for x in range(0,3):
		row = set([game[x][0],game[x][1],game[x][2]])
		if len(row) == 1 and game[x][0] != 0:
			return game[x][0]

	# columns
	for x in range(0,3):
		column = set([game[0][x],game[1][x],game[2][x]])
		if len(column) == 1 and game[0][x] != 0:
			return game[0][x]

	# diagonals
	diagonal1 = set([game[0][0],game[1][1],game[2][2]])
	diagonal2 = set([game[0][2],game[1][1],game[2][0]])
	if len(diagonal1) == 1 or len(diagional2) == 1 and game[1][1] != 0:
		return game[1][1]

	return 0
"""



#def checking_result(game):


