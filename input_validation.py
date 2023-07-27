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


def movement(*info):
    # info is only a move if it is in test_movement,
    # else it is the board and whites turn to use in main game
    if len(info) == 1:
        color = info[0][0]
        name = info[0][1]
        file = info[0][2]
        rank = info[0][3]

        if color == 'W':
            is_white = True
        elif color == 'B':
            is_white = False
        else:
            return []

    else:
        whites_turn = info[0]
        game_board = info[1]

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
        rank = usr_inp[2]
        file = usr_inp[1]

    if name not in valid_pieces:
        print("invalid piece name (hint: has to be lowercase)")
        return []

    if not file_and_rank_in_bounds(file, rank):
        return []

    if len(info) == 1:
        rank = int(rank) - 1
        file = file_to_row[file]

        return [rank, file, name, is_white]

    old_rank = int(usr_inp[2]) - 1
    old_file = file_to_row[usr_inp[1]]

    piece = game_board[old_rank][old_file]

    if not piece:
        print("piece doesn't exist. Try again")
        return []

    if piece.name != name or piece.is_white != whites_turn:
        print("wrong piece. Verify piece is yours")
        return []

    print("\nWhere will your piece move? (e.g. file & rank e3)")
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


def pawn_promotion():
    print("\nWhat will you promote pawn to (n, b, r, q)")
    promotion = input()
    if promotion == "quit":
        quit()
    valid_promotions = ['n', 'b', 'r', 'q']
    for promotions in valid_promotions:
        if promotions == promotion:
            return promotion
    return False
