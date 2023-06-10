from collections import namedtuple

# TODO: make own class
Piece = namedtuple('Piece', ['name', 'is_white'])

def setup():
    board = [[0] * 8 for _ in range(8)]

    # Pawns on Board
    for i in range(8):
        board[1][i] = Piece('p', True)
    for i in range(8):
        board[6][i] = Piece('p', False)

    # Knights on Board
    board[0][1] = Piece('n', True)
    board[0][6] = Piece('n', True)
    board[7][1] = Piece('n', False)
    board[7][6] = Piece('n', False)

    # Bishops on Board
    board[0][2] = Piece('b', True)
    board[0][5] = Piece('b', True)
    board[7][2] = Piece('b', False)
    board[7][5] = Piece('b', False)

    # Rooks on Board
    board[0][0] = Piece('r', True)
    board[0][7] = Piece('r', True)
    board[7][0] = Piece('r', False)
    board[7][7] = Piece('r', False)

    # Queens on Board
    board[0][3] = Piece('q', True)
    board[7][3] = Piece('q', False)

    # Kings on Board
    board[0][4] = Piece('k', True)
    board[7][4] = Piece('k', False)

    return board

def piece_to_str(piece):
    if piece.is_white:
        return "W " + piece.name
    else:
        return "B " + piece.name

def print_board(board):
    horiz_line = " --- --- --- --- --- --- --- ---"
    row = [0] * 8 
    for i in range(len(board)-1, -1, -1):
        print(horiz_line)
        for j in range(8):
            if board[i][j] != 0:
                row[j] = "|" + piece_to_str(board[i][j])
            else:
                row[j] = "|   "
        print(''.join(row) + "|")
    print(horiz_line)
