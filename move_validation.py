from copy import deepcopy


def pawn_move(game_board, *move_info):
    """
       returns: True if pawn move is valid and False if not

       *move_info = [old_rank, new_rank, old_file, new_file, piece]
    """
    old_rank = move_info[0]
    new_rank = move_info[1]
    old_file = move_info[2]
    new_file = move_info[3]
    is_white = move_info[4].is_white

    capture = game_board[new_rank][new_file]
    if (
            abs(old_file - new_file) > 1
            or old_rank == new_rank
            or abs(old_rank - new_rank) > 2
    ):
        return False
    if is_white and new_rank < old_rank:
        return False
    if not is_white and new_rank > old_rank:
        return False

    # validate double move on pawn's first move
    # TODO: incorporate en passent
    if abs(old_rank - new_rank) == 2:
        if old_file != new_file:
            return False
        if is_white:
            if old_rank != 1:
                return False
            else:
                return not game_board[old_rank+1][new_file] and not capture
        if not is_white:
            if old_rank != 6:
                return False
            else:
                return not game_board[old_rank-1][new_file] and not capture

    if old_file == new_file:
        # TODO: check if it reaches the last square and do promotion logic
        return not capture
    else:
        if not capture:
            return False
        else:
            return capture.is_white != is_white


def knight_move(*move_info):
    """
       returns: True if knight move is valid and False if not

       *move_info = [old_rank, new_rank, old_file, new_file, piece]
    """
    old_rank = move_info[0]
    new_rank = move_info[1]
    old_file = move_info[2]
    new_file = move_info[3]

    if abs(old_rank - new_rank) == 2 and abs(old_file - new_file) == 1:
        return True
    elif abs(old_rank - new_rank) == 1 and abs(old_file - new_file) == 2:
        return True
    else:
        return False


def bishop_move(game_board, *move_info):
    """
       returns: True if bishop move is valid and False if not

       *move_info = [old_rank, new_rank, old_file, new_file, piece]
    """
    old_rank = move_info[0]
    new_rank = move_info[1]
    old_file = move_info[2]
    new_file = move_info[3]

    if not abs(old_rank - new_rank) == abs(old_file - new_file):
        return False

    if new_rank > old_rank:
        ranks = list(range(old_rank + 1, new_rank))
    else:
        ranks = list(range(old_rank - 1, new_rank, -1))
    if new_file > old_file:
        files = list(range(old_file + 1, new_file))
    else:
        files = list(range(old_file - 1, new_file, -1))

    for i in range(len(ranks)):
        piece_between = game_board[ranks[i]][files[i]]
        if piece_between:
            return False

    return True


def rook_move(game_board, *move_info):
    """
       returns: True if rook move is valid and False if not

       *move_info = [old_rank, new_rank, old_file, new_file, piece]
    """
    old_rank = move_info[0]
    new_rank = move_info[1]
    old_file = move_info[2]
    new_file = move_info[3]

    if not bool(old_rank - new_rank) ^ bool(old_file - new_file):
        return False

    if new_rank > old_rank:
        ranks = list(range(old_rank + 1, new_rank))
    else:
        ranks = list(range(old_rank - 1, new_rank, -1))
    if new_file > old_file:
        files = list(range(old_file + 1, new_file))
    else:
        files = list(range(old_file - 1, new_file, -1))

    if ranks:
        for i in range(len(ranks)):
            piece_between = game_board[ranks[i]][old_file]
            if piece_between:
                return False

    if files:
        for i in range(len(files)):
            piece_between = game_board[old_rank][files[i]]
            if piece_between:
                return False

    return True


def king_move(game_board, *move_info):
    """
       returns: True if king move is valid and False if not

       *move_info = [old_rank, new_rank, old_file, new_file, piece]
    """

    # TODO: incorporate castling
    if max(abs(move_info[0] - move_info[1]),
           abs(move_info[2] - move_info[3])) > 1:
        return False
    return rook_move(game_board, *move_info) \
        or bishop_move(game_board, *move_info)


def is_possible_move(game_board, *move_info):
    """
       Serves as hub for functions that return the Truthy-ness
       of whether a move is possible

       returns: True if move is valid and False if not

       *move_info = [old_rank, new_rank, old_file, new_file, piece]

    """
    new_rank = move_info[1]
    new_file = move_info[3]
    piece = move_info[4]

    enemy_piece = game_board[new_rank][new_file]
    if enemy_piece and enemy_piece.is_white is piece.is_white:
        return False

    if piece.name == 'p':
        return pawn_move(game_board, *move_info)
    elif piece.name == 'n':
        return knight_move(*move_info)
    elif piece.name == 'b':
        return bishop_move(game_board, *move_info)
    elif piece.name == 'r':
        return rook_move(game_board, *move_info)
    elif piece.name == 'q':
        return bishop_move(game_board, *move_info) \
            or rook_move(game_board, *move_info)
    elif piece.name == 'k':
        return king_move(game_board, *move_info)
    return False


def is_king_checked(king_rank, king_file, king_color, game_board):
    for rank in range(8):
        for file in range(8):
            piece = game_board[rank][file]
            if not piece:
                continue
            if piece.is_white is king_color:
                continue
            move_info = [rank, king_rank, file, king_file, piece]
            if is_possible_move(game_board, *move_info):
                return True
    return False


def attempt_move(king_info, game_board, *move_info):
    """
       This attempts to do the move.

       if the king is checked after attempting the move,
       the move will not happen

       returns True if move is successful and False if not

       move_info = [old_rank, new_rank, old_file, new_file, piece]

    """
    old_rank = move_info[0]
    new_rank = move_info[1]
    old_file = move_info[2]
    new_file = move_info[3]

    piece_to_capture = deepcopy(game_board[new_rank][new_file])
    attacking_piece = deepcopy(game_board[old_rank][old_file])

    game_board[new_rank][new_file] = deepcopy(game_board[old_rank][old_file])
    game_board[old_rank][old_file] = 0

    if is_king_checked(king_info[0], king_info[1], king_info[2], game_board):
        print("cant move here since king would be checked")
        game_board[new_rank][new_file] = piece_to_capture
        game_board[old_rank][old_file] = attacking_piece
        return False
    return True
