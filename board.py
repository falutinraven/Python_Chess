import piece


def setup():
    pieces = []
    board = [[0] * 8 for _ in range(8)]

    # Kings on Board
    board[0][4] = piece.Piece('k', True)
    pieces.append(piece.Piece('k', True, 0, 4))
    board[7][4] = piece.Piece('k', False)
    pieces.append(piece.Piece('k', False, 7, 4))

    # Queens on Board
    board[0][3] = piece.Piece('q', True)
    pieces.append(piece.Piece('q', True, 0, 3))
    board[7][3] = piece.Piece('q', False)
    pieces.append(piece.Piece('q', False, 7, 3))

    # Rooks on Board
    board[0][0] = piece.Piece('r', True)
    pieces.append(piece.Piece('r', True, 0, 0))
    board[0][7] = piece.Piece('r', True)
    pieces.append(piece.Piece('r', True, 0, 7))
    board[7][0] = piece.Piece('r', False)
    pieces.append(piece.Piece('r', False, 7, 0))
    board[7][7] = piece.Piece('r', False)
    pieces.append(piece.Piece('r', False, 7, 7))

    # Bishops on Board
    board[0][2] = piece.Piece('b', True)
    pieces.append(piece.Piece('b', True, 0, 2))
    board[0][5] = piece.Piece('b', True)
    pieces.append(piece.Piece('b', True, 0, 5))
    board[7][2] = piece.Piece('b', False)
    pieces.append(piece.Piece('b', False, 7, 2))
    board[7][5] = piece.Piece('b', False)
    pieces.append(piece.Piece('b', False, 7, 5))

    # Knights on Board
    board[0][1] = piece.Piece('n', True)
    pieces.append(piece.Piece('n', True, 0, 1))
    board[0][6] = piece.Piece('n', True)
    pieces.append(piece.Piece('n', True, 0, 6))
    board[7][1] = piece.Piece('n', False)
    pieces.append(piece.Piece('n', False, 7, 1))
    board[7][6] = piece.Piece('n', False)
    pieces.append(piece.Piece('n', False, 7, 6))

    # Pawns on Board
    for i in range(8):
        board[1][i] = piece.Piece('p', True)
        pieces.append(piece.Piece('p', True, 1, i))
    for i in range(8):
        board[6][i] = piece.Piece('p', False)
        pieces.append(piece.Piece('p', False, 6, i))

    return [pieces, board]


def piece_to_str(piece):
    return "W " + piece.name if piece.is_white else "B " + piece.name


def print_board(board):
    print()
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
    print(horiz_line + "\n")
