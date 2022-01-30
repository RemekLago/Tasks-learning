x = input("How big your board should be? ")
example_board = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
board_size = int(x)

def horizont_line(board_size):
    print(" ----" * board_size)

def vertical_line(board_size):
    print("| 0  " * (board_size) + "|    ")

def printing_board(board_size):
    for i in range(int(board_size)):
            horizont_line(board_size)
            vertical_line(board_size)
    horizont_line(board_size)

printing_board(board_size)