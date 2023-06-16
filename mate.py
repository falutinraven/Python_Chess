import move_validation


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
    old_rank = move_info[0]
    old_file = move_info[2]
    name = move_info[4]
    is_white = move_info[5]

    # theoretical_moves = []
    possible_moves = []

    # north-east
    new_rank = old_rank+1
    new_file = old_file+1
    while True:
        move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
        if move_validation.is_possible_move(game_board, *move_info):
            possible_moves.append(move_info)
            new_rank += 1
            new_file += 1
            continue
        else:
            break

    # south-east
    new_rank = old_rank-1
    new_file = old_file+1
    while True:
        move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
        if move_validation.is_possible_move(game_board, *move_info):
            possible_moves.append(move_info)
            new_rank -= 1
            new_file += 1
            continue
        else:
            break

    # north-west
    new_rank = old_rank+1
    new_file = old_file-1
    while True:
        move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
        if move_validation.is_possible_move(game_board, *move_info):
            possible_moves.append(move_info)
            new_rank += 1
            new_file -= 1
            continue
        else:
            break

    # south-west
    new_rank = old_rank-1
    new_file = old_file-1
    while True:
        move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
        if move_validation.is_possible_move(game_board, *move_info):
            possible_moves.append(move_info)
            new_rank -= 1
            new_file -= 1
            continue
        else:
            break

    return possible_moves


def generate_rook_moves(game_board, *move_info):
    old_rank = move_info[0]
    old_file = move_info[2]
    name = move_info[4]
    is_white = move_info[5]

    # theoretical_moves = []
    possible_moves = []

    # right
    new_rank = old_rank
    new_file = old_file+1
    while True:
        move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
        if move_validation.is_possible_move(game_board, *move_info):
            possible_moves.append(move_info)
            new_file += 1
            continue
        else:
            break

    # left
    new_rank = old_rank
    new_file = old_file-1
    while True:
        move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
        if move_validation.is_possible_move(game_board, *move_info):
            possible_moves.append(move_info)
            new_file -= 1
            continue
        else:
            break

    # up
    new_rank = old_rank+1
    new_file = old_file
    while True:
        move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
        if move_validation.is_possible_move(game_board, *move_info):
            possible_moves.append(move_info)
            new_rank += 1
            continue
        else:
            break

    # down
    new_rank = old_rank-1
    new_file = old_file
    while True:
        move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
        if move_validation.is_possible_move(game_board, *move_info):
            possible_moves.append(move_info)
            new_rank -= 1
            continue
        else:
            break

    return possible_moves


def generate_queen_moves(game_board, *move_info):
    # old_rank = move_info[0]
    # old_file = move_info[2]
    # name = move_info[4]
    # is_white = move_info[5]

    # theoretical_moves = []
    # possible_moves = []

    # for move in theoretical_moves:
    #     new_rank = move[0]
    #     new_file = move[1]
    #     move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
    #     if move_validation.is_possible_move(game_board, *move_info):
    #         possible_moves.append(move_info)

    # return possible_moves
    pass


def generate_king_moves(game_board, *move_info):
    # old_rank = move_info[0]
    # old_file = move_info[2]
    # name = move_info[4]
    # is_white = move_info[5]

    # theoretical_moves = []
    # possible_moves = []

    # for move in theoretical_moves:
    #     new_rank = move[0]
    #     new_file = move[1]
    #     move_info = [old_rank, new_rank, old_file, new_file, name, is_white]
    #     if move_validation.is_possible_move(game_board, *move_info):
    #         possible_moves.append(move_info)

    # return possible_moves

# for move in actual_possible_moves[old_rank][old_file]:
#     if move_attempt == move:
#         return true/move_piece
    pass


def generate_moves():
    """
        make and return a list of all moves that are theoretically possible (call is_possible_move() in move_validation module)
        from whoevers turn it is (whites turn or black) 
        ex: each pawn move will have max of 4 possible moves (not including promotions) and the possible moves will be added
        to a list of all theoretical moves that will be iterated through to check if any prevent check in future function.
    """
    # TODO: use list.extend() instead of append() to take the lists from each of the piece move generators into this final list
    # TODO: confirm piece exists at location of move info. now all the checks are wether the move is possible, but it will do that move even if
    # there is no correct piece at the old_rank and old_file location
    all_possible_moves = []
    all_possible_moves.extend(generate_white_pawn_moves())
    all_possible_moves.extend(generate_black_pawn_moves())
    all_possible_moves.extend(generate_knight_moves())
    all_possible_moves.extend(generate_bishop_moves())
    all_possible_moves.extend(generate_rook_moves())
    all_possible_moves.extend(generate_queen_moves())
    all_possible_moves.extend(generate_king_moves())
    return all_possible_moves


def mate():
    """
       iterate through list of all moves that can be attempted (from generate_moves()) and will attempt_move() each one
       if there is no attempt_move() that succeeds then either checkmate or stalemate (worry about that later)

    """
    pass
