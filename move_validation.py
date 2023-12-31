from copy import deepcopy
import piece


def pawn_move(game_board, *move_info):
    old_rank = move_info[0]
    new_rank = move_info[1]
    old_file = move_info[2]
    new_file = move_info[3]
    is_white = move_info[5]

    capture = game_board[new_rank][new_file]

    if (abs(old_file - new_file) > 1
            or old_rank == new_rank
            or abs(old_rank - new_rank) > 2):
        return False
    if is_white and new_rank < old_rank:
        return False
    if not is_white and new_rank > old_rank:
        return False

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
        return not capture
    else:
        if not capture:
            return False
        else:
            return capture.is_white != is_white


def knight_move(*move_info):
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
    old_rank = move_info[0]
    new_rank = move_info[1]
    old_file = move_info[2]
    new_file = move_info[3]

    if not abs(old_rank - new_rank) == abs(old_file - new_file):
        return False

    if old_rank < new_rank:
        ranks = list(range(old_rank + 1, new_rank))
    else:
        ranks = list(range(old_rank - 1, new_rank, -1))
    if old_file < new_file:
        files = list(range(old_file + 1, new_file))
    else:
        files = list(range(old_file - 1, new_file, -1))

    for i in range(len(ranks)):
        piece_between = game_board[ranks[i]][files[i]]
        if piece_between:
            return False

    return True


def rook_move(game_board, *move_info):
    old_rank = move_info[0]
    new_rank = move_info[1]
    old_file = move_info[2]
    new_file = move_info[3]

    if not bool(old_rank - new_rank) ^ bool(old_file - new_file):
        return False

    min_rank, max_rank = min(old_rank, new_rank), max(old_rank, new_rank)
    min_file, max_file = min(old_file, new_file), max(old_file, new_file)

    ranks = list(range(min_rank + 1, max_rank))
    files = list(range(min_file + 1, max_file))

    for i in range(len(ranks)):
        piece_between = game_board[ranks[i]][old_file]
        if piece_between:
            return False

    for i in range(len(files)):
        piece_between = game_board[old_rank][files[i]]
        if piece_between:
            return False

    return True


def king_move(game_board, *move_info):
    # TODO: incorporate castling
    if max(abs(move_info[0] - move_info[1]),
           abs(move_info[2] - move_info[3])) > 1:
        return False
    return rook_move(game_board, *move_info) \
        or bishop_move(game_board, *move_info)


def is_possible_move(game_board, *move_info):
    """
       *move_info = [old_rank, new_rank, old_file, new_file, name, is_white]

    """
    old_rank = move_info[0]
    old_file = move_info[2]
    new_rank = move_info[1]
    new_file = move_info[3]

    if new_rank < 0 or new_rank > 7:
        return False
    if new_file < 0 or new_file > 7:
        return False

    name = move_info[4]
    is_white = move_info[5]

    p = game_board[old_rank][old_file]
    if not p:
        return False
    if p.name != name or p.is_white is not is_white:
        return False

    enemy_piece = game_board[new_rank][new_file]
    if enemy_piece and enemy_piece.is_white is is_white:
        return False

    if name == 'p':
        return pawn_move(game_board, *move_info)
    elif name == 'n':
        return knight_move(*move_info)
    elif name == 'b':
        return bishop_move(game_board, *move_info)
    elif name == 'r':
        return rook_move(game_board, *move_info)
    elif name == 'q':
        return bishop_move(game_board, *move_info) \
            or rook_move(game_board, *move_info)
    elif name == 'k':
        return king_move(game_board, *move_info)
    return False


def is_king_checked(pieces, game_board, whites_turn):
    king = pieces[0] if whites_turn else pieces[1]

    for p in pieces:
        if not p:
            continue
        if p.is_white == whites_turn:
            continue
        move_info = [p.rank,
                     king.rank,
                     p.file,
                     king.file,
                     p.name,
                     p.is_white]
        if is_possible_move(game_board, *move_info):
            return True
    return False


def attempt_move(pieces, game_board, *move_info):
    """
       This attempts to do the move.

       if the king is checked after attempting the move,
       the move will not happen

       returns True if move is successful and False if not

       move_info = [old_rank, new_rank, old_file, new_file, name, is_white]

    """
    if not is_possible_move(game_board, *move_info):
        return False

    old_rank = move_info[0]
    new_rank = move_info[1]
    old_file = move_info[2]
    new_file = move_info[3]
    name = move_info[4]
    whites_turn = move_info[5]

    piece_to_capture = deepcopy(game_board[new_rank][new_file])
    attacking_piece = deepcopy(game_board[old_rank][old_file])

    game_board[new_rank][new_file] = deepcopy(game_board[old_rank][old_file])
    game_board[old_rank][old_file] = 0

    captured_piece_info = []
    for p in pieces:
        if not p:
            continue
        if p.is_white is not whites_turn:
            continue
        if p.name is not name:
            continue
        if p.rank == old_rank and p.file == old_file:
            p.rank = new_rank
            p.file = new_file
            # piece.name = new_name for promotions
        if p.rank == new_rank and p.file == new_file:
            captured_piece_info = [p.rank,
                                   p.file,
                                   p.name,
                                   p.is_white]
            p = 0

    king_checked = False
    if is_king_checked(pieces, game_board, whites_turn):
        king_checked = True

    game_board[new_rank][new_file] = piece_to_capture
    game_board[old_rank][old_file] = attacking_piece

    for p in pieces:
        if not p:
            if captured_piece_info:
                p = piece.Piece(captured_piece_info[2],
                                captured_piece_info[3],
                                captured_piece_info[0],
                                captured_piece_info[1])
                captured_piece_info = []
            continue
        if p.is_white is not whites_turn:
            continue
        if p.name is not name:
            continue
        if p.rank == new_rank and p.file == new_file:
            p.rank = old_rank
            p.file = old_file
            # piece.name = old_name for promotions

    return not king_checked
