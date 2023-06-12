import move_validation


def piece_moves_white_pawn(game_board, *move_info):
    """
        pass input of piece info and returns a list
        of all of its "valid" moves according to the rules
        (not including check as this will be used to find check)

        return type is list of tuples that are
        [(old_rank1, new_rank1, old_file1, new_file1)....]

        *move_info = [old_rank, new_rank, old_file, new_file, piece]
    """
    old_rank = move_info[0]
    old_file = move_info[2]

    theoretical_moves = [(old_rank+1, old_file), (old_rank+2, old_file),
                         (old_rank+1, old_file+1), (old_rank+1, old_file-1)]
    actual_possible_moves = []

    for move in theoretical_moves:
        # TODO: discard move if its out of bounds.
        move_info = [old_rank, move[0], old_file, move[1]]
        if move_validation.pawn_move(game_board, *move_info):
            actual_possible_moves.append(*move_info)

    return actual_possible_moves


# for move in actual_possible_moves[old_rank][old_file]:
#     if move_attempt == move:
#         return true/move_piece
