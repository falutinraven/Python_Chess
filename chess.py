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

        # move_info = [old_rank, new_rank, old_file, new_file, piece]
        move_info = input_validation.movement(whites_turn, game_board)

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
                white_king_info[0] = move_info[1]
                white_king_info[1] = move_info[3]
            if not whites_turn:
                black_king_info[0] = move_info[1]
                black_king_info[1] = move_info[3]

        piece_index_in_pieces = None 
        capture_index = None
        for i, piece in enumerate(pieces):
            if piece:
                if piece.rank == move_info[1] and piece.file == move_info[3] and piece.is_white != whites_turn:
                    capture_index = i 
            if piece:
                if piece.name == move_info[4].name and piece.is_white == move_info[4].is_white and piece.rank == move_info[0] and piece.file == move_info[2]:
                    piece_index_in_pieces = i
                    break
        if capture_index:
            pieces[capture_index] = None
        if not piece_index_in_pieces:
            print("moved nonexistent piece, try again")
        else:
            pieces[piece_index_in_pieces].rank = move_info[1] 
            pieces[piece_index_in_pieces].file = move_info[3]
            # print(pieces[piece_index_in_pieces].name, pieces[piece_index_in_pieces].rank, pieces[piece_index_in_pieces].file)
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
