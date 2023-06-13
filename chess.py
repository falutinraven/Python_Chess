import board
import move_validation
import input_validation
import piece

white_king_info = [0, 4, True]
black_king_info = [7, 4, False]

def main():
    pieces, game_board = board.setup()
    whites_turn = True
    game_over = False

    while game_over is False:
        board.print_board(game_board)

        # move_info = [old_rank, new_rank, old_file, new_file, move_piece]
        old_rank, new_rank, old_file, new_file, move_piece = input_validation.movement(whites_turn, game_board)

        move_info = [old_rank, new_rank, old_file, new_file, move_piece]

        if not move_info:
            continue

        # TODO: put is possible move in attempt move in move_validation module.
        if whites_turn:
            successful_move = move_validation.attempt_move(
                white_king_info,
                game_board,
                *move_info)
        else:
            successful_move = move_validation.attempt_move(
                black_king_info,
                game_board,
                *move_info)

        if not successful_move:
            print("invalid move, try again")
            continue

        if move_info[-1] == 'k':
            if whites_turn:
                white_king_info[0] = new_rank
                white_king_info[1] = new_file
            if not whites_turn:
                black_king_info[0] = new_rank
                black_king_info[1] = new_file

        piece_index = None 
        capture_index = None
        for i, piece in enumerate(pieces):
            if piece:
                if piece.rank == new_rank and piece.file == new_file and piece.is_white != whites_turn:
                    capture_index = i 
            if piece:
                if piece.name == move_piece.name and piece.is_white == move_piece.is_white and piece.rank == old_rank and piece.file == old_file:
                    piece_index_in_pieces = i
                    break
        if capture_index:
            pieces[capture_index] = None
        if not piece_index:
            print("moved nonexistent piece, try again")
        else:
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
