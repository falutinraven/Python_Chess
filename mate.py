import move_validation


def directional_moves(game_board, vertical, horizontal, *move_info):
    """
        vertical   = rate of change  (1 = up,    0 = no change, -1 = down)
        horizontal = rate of change  (1 = right, 0 = no change, -1 = left)

        *move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
    """
    old_rank = move_info[0]
    old_file = move_info[2]
    name = move_info[4]
    is_white = move_info[5]

    possible_moves = []

    new_rank = old_rank + vertical
    new_file = old_file + horizontal

    while True:
        move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
        if not move_validation.is_possible_move(game_board, *move_info):
            break
        possible_moves.append(move_info)
        new_file += horizontal
        new_rank += vertical

    return possible_moves


def filter_moves(game_board, theoretical_moves, *move_info):
    """
        *move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
    """
    old_rank = move_info[0]
    old_file = move_info[2]
    name = move_info[4]
    is_white = move_info[5]

    possible_moves = []

    for move in theoretical_moves:
        new_rank = move[0]
        new_file = move[1]

        move_info = [old_rank, new_rank, old_file, new_file, name, is_white]

        if move_validation.is_possible_move(game_board, *move_info):
            possible_moves.append(move_info)

    return possible_moves


def white_pawn_moves(game_board, *move_info):
    """
        *move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
    """
    old_rank = move_info[0]
    old_file = move_info[2]

    theoretical_moves = [(old_rank+1, old_file),
                         (old_rank+2, old_file),
                         (old_rank+1, old_file+1),
                         (old_rank+1, old_file-1)]

    return filter_moves(game_board, theoretical_moves, *move_info)


def black_pawn_moves(game_board, *move_info):
    """
        *move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
    """

    old_rank = move_info[0]
    old_file = move_info[2]

    theoretical_moves = [(old_rank-1, old_file),
                         (old_rank-2, old_file),
                         (old_rank-1, old_file+1),
                         (old_rank-1, old_file-1)]

    return filter_moves(game_board, theoretical_moves, *move_info)


def knight_moves(game_board, *move_info):
    """
        *move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
    """
    old_rank = move_info[0]
    old_file = move_info[2]

    theoretical_moves = [(old_rank+1, old_file+2),
                         (old_rank+2, old_file+1),
                         (old_rank-1, old_file+2),
                         (old_rank+2, old_file-1),
                         (old_rank-2, old_file+1),
                         (old_rank+1, old_file-2),
                         (old_rank-1, old_file-2),
                         (old_rank-2, old_file-1)]

    return filter_moves(game_board, theoretical_moves, *move_info)


def bishop_moves(game_board, *move_info):
    possible_moves = []

    north_east = directional_moves(game_board, 1, 1, *move_info)
    possible_moves.extend(north_east)

    south_east = directional_moves(game_board, -1, 1, *move_info)
    possible_moves.extend(south_east)

    north_west = directional_moves(game_board, 1, -1, *move_info)
    possible_moves.extend(north_west)

    south_west = directional_moves(game_board, -1, -1, *move_info)
    possible_moves.extend(south_west)

    return possible_moves


def rook_moves(game_board, *move_info):
    possible_moves = []

    right = directional_moves(game_board, 0, 1, *move_info)
    possible_moves.extend(right)

    left = directional_moves(game_board, 0, -1, *move_info)
    possible_moves.extend(left)

    up = directional_moves(game_board, 1, 0, *move_info)
    possible_moves.extend(up)

    down = directional_moves(game_board, -1, 0, *move_info)
    possible_moves.extend(down)

    return possible_moves


def king_moves(game_board, *move_info):
    """
        *move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
    """
    old_rank = move_info[0]
    old_file = move_info[2]

    # TODO: include castling
    theoretical_moves = [(old_rank+1, old_file+1),
                         (old_rank+1, old_file),
                         (old_rank+1, old_file-1),
                         (old_rank, old_file+1),
                         (old_rank, old_file-1),
                         (old_rank-1, old_file+1),
                         (old_rank-1, old_file),
                         (old_rank-1, old_file-1)]

    return filter_moves(game_board, theoretical_moves, *move_info)


def generate_moves(pieces, whites_turn, game_board):
    """
        *move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
    """

    moves = []

    for piece in pieces:
        if not piece:
            continue
        if piece.is_white is not whites_turn:
            continue

        move_info = [piece.rank,
                     None,
                     piece.file,
                     None,
                     piece.name,
                     piece.is_white]

        if piece.name == 'p' and piece.is_white:
            moves.extend(white_pawn_moves(game_board, *move_info))
        if piece.name == 'p' and not piece.is_white:
            moves.extend(black_pawn_moves(game_board, *move_info))
        if piece.name == 'n':
            moves.extend(knight_moves(game_board, *move_info))
        if piece.name == 'b':
            moves.extend(bishop_moves(game_board, *move_info))
        if piece.name == 'r':
            moves.extend(rook_moves(game_board, *move_info))
        if piece.name == 'q':
            moves.extend(bishop_moves(game_board, *move_info))
            moves.extend(rook_moves(game_board, *move_info))
        if piece.name == 'k':
            moves.extend(king_moves(game_board, *move_info))

    return moves


def mate(pieces, whites_turn, game_board):
    all_possible_moves = generate_moves(pieces, whites_turn, game_board)
    for move_info in all_possible_moves:
        if move_validation.attempt_move(pieces, game_board, *move_info):
            return False
    if move_validation.is_king_checked(pieces, game_board, whites_turn):
        victor = "Black" if whites_turn else "White"
        print("checkmate: " + victor + " wins\n")
    else:
        print("stalemate: Draw\n")
    return True
