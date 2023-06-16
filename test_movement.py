import unittest
import move_validation as validate
from collections import namedtuple

file_to_row = {'A': 0, 'a': 0, 'B': 1, 'b': 1, 'C': 2, 'c': 2,
               'D': 3, 'd': 3, 'E': 4, 'e': 4, 'F': 5, 'f': 5,
               'G': 6, 'g': 6, 'H': 7, 'h': 7}
white = True
black = False
Piece = namedtuple('Piece', ['name', 'is_white'])
file = file_to_row['e']


class TestWhitePawn(unittest.TestCase):
    def test_forwards_and_backwards(self):
        new_board = [[0] * 8 for _ in range(8)]
        new_board[4][file] = Piece('p', white)
        move_info = [4, 5, file, file, 'p', white]
        forwards_move = validate.is_possible_move(new_board, *move_info)
        self.assertTrue(forwards_move)

        new_board = [[0] * 8 for _ in range(8)]
        new_board[5][file] = Piece('p', white)
        move_info = [5, 4, file, file, 'p', white]
        backwards_move = validate.is_possible_move(new_board, *move_info)
        self.assertFalse(backwards_move)

    def test__capture(self):
        new_board = [[0] * 8 for _ in range(8)]
        move_info = [4, 5, file-1, file, 'p', white]

        new_board = [[0] * 8 for _ in range(8)]
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        empty_capture = validate.is_possible_move(new_board, *move_info)
        self.assertFalse(empty_capture)

        new_board = [[0] * 8 for _ in range(8)]
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        new_board[5][file] = Piece('p', black)
        valid_capture = validate.is_possible_move(new_board, *move_info)
        self.assertTrue(valid_capture)

        new_board = [[0] * 8 for _ in range(8)]
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        new_board[5][file] = Piece('p', white)
        invalid_capture = validate.is_possible_move(new_board, *move_info)
        self.assertFalse(invalid_capture)

    def test_two_spaces(self):
        new_board = [[0] * 8 for _ in range(8)]
        move_info = [1, 3, file, file, 'p', white]
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        from_starting_point = validate.is_possible_move(new_board, *move_info)
        self.assertTrue(from_starting_point)

        new_board = [[0] * 8 for _ in range(8)]
        move_info = [2, 4, file, file, 'p', white]
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        from_other_row = validate.is_possible_move(new_board, *move_info)
        self.assertFalse(from_other_row)

    def test_obstructed(self):
        new_board = [[0] * 8 for _ in range(8)]
        move_info = [1, 3, file, file, 'p', white]
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        not_obstructed = validate.is_possible_move(new_board, *move_info)
        self.assertTrue(not_obstructed)

        new_board = [[0] * 8 for _ in range(8)]
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        new_board[2][file] = Piece('p', black)
        obstructed = validate.is_possible_move(new_board, *move_info)
        self.assertFalse(obstructed)


class TestBlackPawn(unittest.TestCase):
    def test_forwards_and_backwards(self):
        new_board = [[0] * 8 for _ in range(8)]
        move_info = [5, 4, file, file, 'p', black]
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        forwards_move = validate.is_possible_move(new_board, *move_info)
        self.assertTrue(forwards_move)

        new_board = [[0] * 8 for _ in range(8)]
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        move_info = [4, 5, file, file, 'p', black]
        backwards_move = validate.is_possible_move(new_board, *move_info)
        self.assertFalse(backwards_move)

    def test_capture(self):
        new_board = [[0] * 8 for _ in range(8)]
        move_info = [7, 6, file-1, file, 'p', black]
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        empty_capture = validate.is_possible_move(new_board, *move_info)
        self.assertFalse(empty_capture)

        new_board[6][file] = Piece('p', white)
        valid_capture = validate.is_possible_move(new_board, *move_info)
        self.assertTrue(valid_capture)

        new_board[6][file] = Piece('p', black)
        invalid_capture = validate.is_possible_move(new_board, *move_info)
        self.assertFalse(invalid_capture)

    def test_two_spaces(self):
        new_board = [[0] * 8 for _ in range(8)]
        move_info = [6, 4, file, file, 'p', black]
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        from_starting_point = validate.is_possible_move(new_board, *move_info)
        self.assertTrue(from_starting_point)

        move_info = [5, 3, file, file, 'p', black]
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        from_other_row = validate.is_possible_move(new_board, *move_info)
        self.assertFalse(from_other_row)

    def test_obstructed(self):
        new_board = [[0] * 8 for _ in range(8)]
        move_info = [6, 4, file, file, 'p', black]
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        unobstructed = validate.is_possible_move(new_board, *move_info)
        new_board[4][file] = Piece('p', False)
        obstructed = validate.is_possible_move(new_board, *move_info)
        self.assertFalse(obstructed)
        self.assertTrue(unobstructed)


class TestBishop(unittest.TestCase):
    def test_distance_one(self):
        new_board = [[0] * 8 for _ in range(8)]
        move_info = [4, 5, file, file+1, 'b', white]
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        north_east = validate.is_possible_move(new_board, *move_info)

        move_info[0] = 5
        move_info[1] = 4
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        south_east = validate.is_possible_move(new_board, *move_info)

        move_info[3] = file - 1
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        south_west = validate.is_possible_move(new_board, *move_info)

        move_info[0] = 4
        move_info[1] = 5
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        north_west = validate.is_possible_move(new_board, *move_info)

        self.assertTrue(north_east)
        self.assertTrue(south_east)
        self.assertTrue(south_west)
        self.assertTrue(north_west)

    def test_capture(self):
        new_board = [[0] * 8 for _ in range(8)]
        move_info = [3, 5, file-2, file, 'b', white]
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])

        new_board[5][file] = Piece('p', black)
        valid_capture = validate.is_possible_move(new_board, *move_info)
        self.assertTrue(valid_capture)

        new_board[5][file] = Piece('p', white)
        invalid_capture = validate.is_possible_move(new_board, *move_info)
        self.assertFalse(invalid_capture)

    def test_obstructed(self):
        new_board = [[0] * 8 for _ in range(8)]
        move_info = [2, 6, file-4, file, 'b', white]
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        not_obstructed = validate.is_possible_move(new_board, *move_info)
        self.assertTrue(not_obstructed)

        new_board[3][file-3] = Piece('p', black)
        obstructed = validate.is_possible_move(new_board, *move_info)
        self.assertFalse(obstructed)


class TestRook(unittest.TestCase):
    def test_normal(self):
        new_board = [[0] * 8 for _ in range(8)]
        move_info = [2, 5, file, file, 'r', white]
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        north = validate.is_possible_move(new_board, *move_info)

        move_info[0] = 6
        move_info[1] = 4
        new_board = [[0] * 8 for _ in range(8)]
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        south = validate.is_possible_move(new_board, *move_info)

        move_info = [4, 4, file_to_row['a'], file, 'r', white]
        new_board = [[0] * 8 for _ in range(8)]
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        east = validate.is_possible_move(new_board, *move_info)

        move_info[2], move_info[3] = move_info[3], move_info[2]
        new_board = [[0] * 8 for _ in range(8)]
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        west = validate.is_possible_move(new_board, *move_info)

        self.assertTrue(north)
        self.assertTrue(south)
        self.assertTrue(east)
        self.assertTrue(west)

    def test_capture(self):
        new_board = [[0] * 8 for _ in range(8)]
        move_info = [0, 5, file, file, 'r', white]
        new_board[5][file] = Piece('p', black)
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        valid_capture = validate.is_possible_move(new_board, *move_info)

        new_board[5][file] = Piece('p', white)
        invalid_capture = validate.is_possible_move(new_board, *move_info)

        self.assertTrue(valid_capture)
        self.assertFalse(invalid_capture)

    def test_obstructed(self):
        new_board = [[0] * 8 for _ in range(8)]
        move_info = [1, 6, file, file, 'r', white]
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        not_obstructed = validate.is_possible_move(new_board, *move_info)

        new_board[3][file] = Piece('p', black)
        obstructed = validate.is_possible_move(new_board, *move_info)

        self.assertTrue(not_obstructed)
        self.assertFalse(obstructed)


class TestKnight(unittest.TestCase):
    def test_normal(self):
        new_board = [[0] * 8 for _ in range(8)]
        move_info = [4, 6, file, file-1, 'n', white]
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        move = validate.is_possible_move(new_board, *move_info)

        move_info = [4, 7, file, file-1, 'n', white]
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        bad_move = validate.is_possible_move(new_board, *move_info)
        self.assertTrue(move)
        self.assertFalse(bad_move)

    def test_capture(self):
        new_board = [[0] * 8 for _ in range(8)]
        move_info = [4, 6, file, file-1, 'n', white]
        new_board[move_info[0]][move_info[2]] = Piece(move_info[4],
                                                      move_info[5])
        new_board[6][file-1] = Piece('p', black)
        valid_capture = validate.is_possible_move(new_board, *move_info)

        new_board[6][file-1] = Piece('p', white)
        invalid_capture = validate.is_possible_move(new_board, *move_info)

        self.assertTrue(valid_capture)
        self.assertFalse(invalid_capture)

# TODO: make unit tests with checked king
