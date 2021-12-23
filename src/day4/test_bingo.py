import random
from unittest import TestCase

from src.day4.bingo import BingoBoard, play_bingo


class BingoBoardTest(TestCase):
    def test_new_bingo_board_has_not_yet_won(self):
        board = BingoBoard(list(range(25)))
        self.assertFalse(board.has_won())

    def test_bingo_board_wins_after_5_easy_moves(self):
        board = BingoBoard(list(range(25)))
        for i in range(5):
            board.mark(i)
        self.assertTrue(board.has_won())

    def test_bingo_board_does_not_win_after_a_number_of_non_winning_moves(self):
        board = BingoBoard(list(range(25)))
        moves = [0, 3, 5, 7, 8, 9, 12, 14, 18, 21, 24]
        for i in moves:
            board.mark(i)
        self.assertFalse(board.has_won())

    def test_bingo_board_wins_after_5_easy_moves_in_reverse(self):
        board = BingoBoard(list(range(25)))
        moves = list(range(5))
        moves.reverse()
        for i in moves:
            board.mark(i)
        self.assertTrue(board.has_won())

    def test_bingo_board_wins_after_5_easy_moves_in_the_2nd_row(self):
        board = BingoBoard(list(range(25)))
        moves = list(range(5, 10))
        for i in moves:
            board.mark(i)
        self.assertTrue(board.has_won())

    def test_bingo_board_wins_after_5_easy_moves_in_the_5th_row(self):
        board = BingoBoard(list(range(25)))
        moves = list(range(20, 25))
        for i in moves:
            board.mark(i)
        self.assertTrue(board.has_won())

    def test_bingo_board_wins_after_5_vertical_moves(self):
        board = BingoBoard(list(range(25)))
        moves = list(range(0, 25, 5))
        for i in moves:
            board.mark(i)
        self.assertTrue(board.has_won())

    def test_bingo_board_wins_after_more_than_5_moves(self):
        board = BingoBoard(list(range(25)))
        win_moves = list(range(20, 25))
        other_moves = [0, 4, 8, 9]
        all_moves = win_moves + other_moves
        random.shuffle(all_moves)

        for i in all_moves:
            board.mark(i)
        self.assertTrue(board.has_won())

    def test_board_can_be_created_from_a_string(self):
        board = BingoBoard.from_string_input(
            """14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""
        )
        moves = (
            7,
            4,
            9,
            5,
            11,
            17,
            23,
            2,
            0,
            14,
            21,
            24,
            10,
            16,
            13,
            6,
            15,
            25,
            12,
            22,
            18,
            20,
            8,
            19,
            3,
            26,
            1,
        )
        for move in moves:
            board.mark(move)
        self.assertTrue(board.has_won())

    def test_returns_non_marked_cells(self):
        random_numbers = [random.randint(0, 100) for _ in range(25)]
        board = BingoBoard(random_numbers)
        for i in random_numbers[:5]:
            board.mark(i)
        self.assertEqual(board.non_marked_cells(), random_numbers[5:])


class PlayBingoTest(TestCase):
    def test_can_parse_a_string_and_play_the_bingo_game(self):
        winning_board, last_move = play_bingo(
            """0,1,2,3,4

 0  1  2  3  4
 5  6  7  8  9
10 11 12 13 14
15 16 17 18 19
20 21 22 23 24
"""
        )
        self.assertTrue(winning_board.has_won())
        self.assertEqual(winning_board.non_marked_cells(), list(range(5, 25)))
        self.assertEqual(last_move, 4)

    def test_can_play_the_sample_game_and_win(self):
        winning_board, last_move = play_bingo(
            """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""
        )
        expected_winner_board = BingoBoard.from_string_input(
            """14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
        )
        self.assertEqual(winning_board, expected_winner_board)
        self.assertEqual(sum(winning_board.non_marked_cells()), 188)
        self.assertEqual(last_move, 24)
