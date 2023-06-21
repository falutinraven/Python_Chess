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
            # TODO: implement different mates i.e. checkmate/stalemate
            if whites_turn:
                print("game over: black wins")
            if not whites_turn:
                print("game over: white wins")
                pass
            break

        # move_info = [old_rank, new_rank, old_file, new_file, move_piece]
        move_info = input_validation.movement(whites_turn, game_board)

        if not move_info:
            continue

        old_rank = move_info[0]
        new_rank = move_info[1]
        old_file = move_info[2]
        new_file = move_info[3]
        move_piece_name = move_info[4]
        move_piece_is_white = move_info[5]

        # TODO: put is possible move in attempt move in move_validation module.
        successful_move = move_validation.attempt_move(
            pieces,
            game_board,
            *move_info)

        if not successful_move:
            print("invalid move, try again")
            continue

        # move piece if successful move
        game_board[new_rank][new_file] = deepcopy(game_board[old_rank][old_file])
        game_board[old_rank][old_file] = 0

        piece_index = None
        capture_index = None
        for i, piece in enumerate(pieces):
            if not piece:
                continue
            if piece.rank == new_rank and piece.file == new_file and piece.is_white != whites_turn:
                capture_index = i
            if piece.name == move_piece_name and piece.is_white == move_piece_is_white and piece.rank == old_rank and piece.file == old_file:
                piece_index = i
                break
        if capture_index:
            pieces[capture_index] = None
        if not piece_index:
            print("moved nonexistent piece, try again")
            continue
        pieces[piece_index].rank = new_rank
        pieces[piece_index].file = new_file
        # print(pieces[piece_index].name, pieces[piece_index].rank, pieces[piece_index].file)
        # pieces[i].name = name if promoting pawn
        """
        for the piece that I move i will check if there is no piece where it used to be.
        i also need to make sure to remember to store its old location so i can find the right piece
        in the list of pieces

        after successful move, i will update the pieces location in the list of pieces
        i will also double check that the board contains the right piece at the right location
        """
        whites_turn = not whites_turn


if __name__ == "__main__":
    main()
