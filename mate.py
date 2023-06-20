import move_validation


def generate_directional_moves(game_board, vertical, horizontal, *move_info):
    """
        vertical is the rate of change  (1 = up, 0 = no change, -1 = down)
        horizontal is the rate of change (1 = right, 0 = no change, -1 = left)
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


def generate_white_pawn_moves(game_board, *move_info):
    """
        pass input of piece info and returns a list
        of all of its "valid" moves according to the rules
        (not including check as this will be used to find check)

        return type is list of tuples that are
        [(old_rank1, new_rank1, old_file1, new_file1)....]

        *move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
    """
    old_rank = move_info[0]
    old_file = move_info[2]
    name = move_info[4]
    is_white = move_info[5]

    theoretical_moves = [(old_rank+1, old_file), (old_rank+2, old_file),
                         (old_rank+1, old_file+1), (old_rank+1, old_file-1)]
    possible_moves = []

    for move in theoretical_moves:
        new_rank = move[0]
        new_file = move[1]
        move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
        if move_validation.is_possible_move(game_board, *move_info):
            possible_moves.append(move_info)

    return possible_moves


def generate_black_pawn_moves(game_board, *move_info):
    """
        pass input of piece info and returns a list
        of all of its "valid" moves according to the rules
        (not including check as this will be used to find check)

        return type is list of tuples that are
        [(old_rank1, new_rank1, old_file1, new_file1)....]

        *move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
    """
    old_rank = move_info[0]
    old_file = move_info[2]
    name = move_info[4]
    is_white = move_info[5]

    theoretical_moves = [(old_rank-1, old_file), (old_rank-2, old_file),
                         (old_rank-1, old_file+1), (old_rank-1, old_file-1)]
    possible_moves = []

    for move in theoretical_moves:
        new_rank = move[0]
        new_file = move[1]
        move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
        if move_validation.is_possible_move(game_board, *move_info):
            possible_moves.append(move_info)

    return possible_moves


def generate_knight_moves(game_board, *move_info):
    old_rank = move_info[0]
    old_file = move_info[2]
    name = move_info[4]
    is_white = move_info[5]

    theoretical_moves = [(old_rank+1, old_file+2),
                         (old_rank+2, old_file+1),
                         (old_rank-1, old_file+2),
                         (old_rank+2, old_file-1),
                         (old_rank-2, old_file+1),
                         (old_rank+1, old_file-2),
                         (old_rank-1, old_file-2),
                         (old_rank-2, old_file-1)]
    possible_moves = []

    for move in theoretical_moves:
        new_rank = move[0]
        new_file = move[1]
        move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
        if move_validation.is_possible_move(game_board, *move_info):
            possible_moves.append(move_info)

    return possible_moves


def generate_bishop_moves(game_board, *move_info):
    possible_moves = []

    north_east = generate_directional_moves(game_board, 1, 1, *move_info)
    possible_moves.extend(north_east)
    south_east = generate_directional_moves(game_board, -1, 1, *move_info)
    possible_moves.extend(south_east)
    north_west = generate_directional_moves(game_board, 1, -1, *move_info)
    possible_moves.extend(north_west)
    south_west = generate_directional_moves(game_board, -1, -1, *move_info)
    possible_moves.extend(south_west)

    return possible_moves


def generate_rook_moves(game_board, *move_info):
    possible_moves = []

    right = generate_directional_moves(game_board, 0, 1, *move_info)
    possible_moves.extend(right)
    left = generate_directional_moves(game_board, 0, -1, *move_info)
    possible_moves.extend(left)
    up = generate_directional_moves(game_board, 1, 0, *move_info)
    possible_moves.extend(up)
    down = generate_directional_moves(game_board, -1, 0, *move_info)
    possible_moves.extend(down)

    return possible_moves


def generate_king_moves(game_board, *move_info):
    old_rank = move_info[0]
    old_file = move_info[2]
    name = move_info[4]
    is_white = move_info[5]

    # TODO: include castling
    theoretical_moves = [(old_rank+1, old_file+1),
                         (old_rank+1, old_file),
                         (old_rank+1, old_file-1),
                         (old_rank, old_file+1),
                         (old_rank, old_file-1),
                         (old_rank-1, old_file+1),
                         (old_rank-1, old_file),
                         (old_rank-1, old_file-1)]
    possible_moves = []

    for move in theoretical_moves:
        new_rank = move[0]
        new_file = move[1]
        move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
        if move_validation.is_possible_move(game_board, *move_info):
            possible_moves.append(move_info)

    return possible_moves


def generate_moves(pieces, whites_turn, game_board):
    """
        make and return a list of all moves that are theoretically possible (call is_possible_move() in move_validation module)
        from whoevers turn it is (whites turn or black)
        ex: each pawn move will have max of 4 possible moves (not including promotions) and the possible moves will be added
        to a list of all theoretical moves that will be iterated through to check if any prevent check in future function.

        *move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
    """
    all_possible_moves = []

    for piece in pieces:
        move_info = [piece.rank, None, piece.file, None, piece.name, piece.is_white]
        if not piece:
            continue
        if piece.is_white is not whites_turn:
            continue
        if piece.name == 'p':
            if piece.is_white:
                all_possible_moves.extend(generate_white_pawn_moves(game_board,
                                                                    *move_info))
            else:
                all_possible_moves.extend(generate_black_pawn_moves(game_board,
                                                                    *move_info))
        if piece.name == 'n':
            all_possible_moves.extend(generate_knight_moves(game_board,
                                                            *move_info))
        if piece.name == 'b':
            all_possible_moves.extend(generate_bishop_moves(game_board,
                                                            *move_info))
        if piece.name == 'r':
            all_possible_moves.extend(generate_rook_moves(game_board,
                                                          *move_info))
        if piece.name == 'q':
            all_possible_moves.extend(generate_bishop_moves(game_board,
                                                            *move_info))
            all_possible_moves.extend(generate_rook_moves(game_board,
                                                          *move_info))
        if piece.name == 'k':
            all_possible_moves.extend(generate_king_moves(game_board,
                                                          *move_info))

    return all_possible_moves


def mate(pieces, whites_turn, game_board):
    """
       iterate through list of all moves that can be attempted (from generate_moves()) and will attempt_move() each one
       if there is no attempt_move() that succeeds then either checkmate or stalemate (worry about that later)
       TODO: make attempt_move not actually move piece if piece can be moved

    """
    all_possible_moves = generate_moves(pieces, whites_turn, game_board)
    for move_info in all_possible_moves:
        if move_validation.attempt_move(pieces, game_board, *move_info):
            print("whites turn = ", whites_turn)
            print("ranks, ",
                  move_info[0]+1, " ",
                  move_info[1]+1, " ",)

            print("files, ",
                  move_info[2]+1, " ",
                  move_info[3]+1, " ",)

            print(move_info[4], " ",
                  move_info[5])
            return False
    return True
