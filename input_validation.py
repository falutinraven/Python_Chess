file_to_row = {'A': 0, 'a': 0, 'B': 1, 'b': 1, 'C': 2, 'c': 2,
               'D': 3, 'd': 3, 'E': 4, 'e': 4, 'F': 5, 'f': 5,
               'G': 6, 'g': 6, 'H': 7, 'h': 7}
valid_pieces = set({'p', 'n', 'b', 'r', 'q', 'k'})


def file_and_rank_in_bounds(file, rank):
    if file not in file_to_row:
        print("file not valid try again")
        return False
    if not rank.isdigit() or int(rank) < 1 or int(rank) > 8:
        print("rank is a number 1-8, try again")
        return False
    return True


def movement(whites_turn, game_board):
    """
        returns move_info if valid input. if not, returns an empty list
        move_info = [old_rank, new_rank, old_file, new_file, piece]
    """
    turn = "White" if whites_turn else "Black"

    print(turn + "'s turn: input letter, file & rank of piece to move")
    print("pieces: (p, n, b, r, q, k), file: A/a-H/h, rank: 1-8")

    usr_inp = input()

    if usr_inp == "quit":
        quit()

    if len(usr_inp) != 3:
        print("input too long/short. 'pe2' for pawn on file E and rank 2")
        return []

    name = usr_inp[0]

    if name not in valid_pieces:
        print("invalid piece name (hint: has to be lowercase)")
        return []

    if not file_and_rank_in_bounds(usr_inp[1], usr_inp[2]):
        return []

    old_rank = int(usr_inp[2]) - 1
    old_file = file_to_row[usr_inp[1]]

    piece = game_board[old_rank][old_file]

    if not piece:
        print("piece doesn't exist. Try again")
        return []

    if piece.name != name or piece.is_white != whites_turn:
        print("wrong piece. Verify piece is yours")
        return []

    print()
    print("Where will your piece move? (e.g. file & rank e3)")
    move = input()
    if move == "quit":
        quit()

    if len(move) != 2:
        print("make input just 2 letters")
        return []

    if not file_and_rank_in_bounds(move[0], move[1]):
        return []

    new_rank = int(move[1]) - 1
    new_file = file_to_row[move[0]]

    return [old_rank, new_rank, old_file, new_file, piece.name, piece.is_white]
