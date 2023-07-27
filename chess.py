import board
import move_validation
import input_validation
import mate
from copy import deepcopy


def main():
    pieces, game_board = board.setup()
    whites_turn = True

    while True:
        board.print_board(game_board)

        if mate.mate(pieces, whites_turn, game_board):
            break

        move_info = input_validation.movement(whites_turn, game_board)
        if not move_info:
            continue

        old_rank = move_info[0]
        new_rank = move_info[1]
        old_file = move_info[2]
        new_file = move_info[3]

        successful_move = move_validation.attempt_move(
            pieces,
            game_board,
            *move_info)

        if not successful_move:
            print("invalid move, try again")
            continue

        piece_to_move = deepcopy(game_board[old_rank][old_file])
        game_board[new_rank][new_file] = piece_to_move
        game_board[old_rank][old_file] = 0

        piece_index = None
        capture_index = None
        for i, piece in enumerate(pieces):
            if not piece:
                continue
            if piece.rank == new_rank and piece.file == new_file:
                capture_index = i
            if piece.rank == old_rank and piece.file == old_file:
                piece_index = i
        if capture_index:
            pieces[capture_index] = None

        pieces[piece_index].rank = new_rank
        pieces[piece_index].file = new_file

        if piece_to_move.name == 'p':
            if new_rank == 7 or new_rank == 0:
                while True:
                    promotion = input_validation.pawn_promotion()
                    if not promotion:
                        print("Type in valid promotion")
                        continue
                    pieces[i].name = promotion
                    game_board[new_rank][new_file].name = promotion
                    break

        whites_turn = not whites_turn


if __name__ == "__main__":
    main()
