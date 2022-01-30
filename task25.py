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
                print(score)
            else:
                score = 0
            print(score)

def checking_diagonals(game):
    score = 0
    for j in range(3):
        for i in range(1):
            if game[i][j] == game[i+1][j] == game[i+2][j]:
                score = 1
                print(score)
            else:
                score = 0
            print(score)

checking_columns(game_1)



#def checking_result(game):


