import board
import move_validation
import input_validation

white_king_info = [0, 4, True]
black_king_info = [7, 4, False]


def main():
    game_board = board.setup()
    whites_turn = True
    game_over = False

    while game_over is False:
        board.print_board(game_board)

        # move_info = [old_rank, new_rank, old_file, new_file, piece]
        move_info = input_validation.movement(whites_turn, game_board)

        if not move_info:
            continue

        # TODO: put is possible move in attempt move in move_validation module.
        if move_validation.is_possible_move(game_board, *move_info):
            if whites_turn:

                successful_move = move_validation.attempt_move(
                    white_king_info,
                    game_board,
                    *move_info)

            if not whites_turn:

                successful_move = move_validation.attempt_move(
                    black_king_info,
                    game_board,
                    *move_info)

            if not successful_move:
                print("Prevent check to make move valid, try again")
                continue

        else:
            print("not a valid move")
            continue

        if move_info[-1] == 'k':
            if whites_turn:
                white_king_info[0] = move_info[1]
                white_king_info[1] = move_info[3]
            if not whites_turn:
                black_king_info[0] = move_info[1]
                black_king_info[1] = move_info[3]

        whites_turn = not whites_turn


if __name__ == "__main__":
    main()
