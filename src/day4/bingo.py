from src.inputs.inputs import get_raw_input


class BingoBoard:
    horizontal_wins_indexes = [
        set(range(lower_step, lower_step + 5)) for lower_step in range(0, 25, 5)
    ]
    vertical_wins_indexes = [
        set(range(lower_step, 25, 5)) for lower_step in range(0, 5)
    ]
    all_wins_indexes = horizontal_wins_indexes + vertical_wins_indexes

    def __init__(self, cells):
        self.cells = cells
        self.marked_cells = []

    @staticmethod
    def from_string_input(input_string: str) -> "BingoBoard":
        cells = []
        for line in input_string.split("\n"):
            for cell in line.split(" "):
                if cell:
                    cells.append(int(cell))

        return BingoBoard(cells)

    def mark(self, move):
        if move in self.cells:
            index = self.cells.index(move)
            self.marked_cells.append(index)
            self.marked_cells.sort()

    def has_won(self):
        for win in self.all_wins_indexes:
            if set(self.marked_cells) >= win:
                return True
        return False

    def non_marked_cells(self):
        non_marked = []
        for i in range(len(self.cells)):
            if i not in self.marked_cells:
                non_marked.append(self.cells[i])
        return non_marked

    def __eq__(self, other):
        return self.cells == other.cells


def parse_input(input_string):
    [inputs_string, *boards_strings] = input_string.split("\n\n")
    moves = [int(input_value) for input_value in inputs_string.split(",")]
    boards = [
        BingoBoard.from_string_input(board_string) for board_string in boards_strings
    ]
    return boards, moves


def play_bingo(input_string: str) -> (BingoBoard, int):
    boards, moves = parse_input(input_string)
    for i in moves:
        for board in boards:
            board.mark(i)
            if board.has_won():
                return board, i


def play_to_lose(input_string: str) -> (BingoBoard, int):
    boards, moves = parse_input(input_string)
    last_winner_board = None
    last_winner_move = None
    for i in moves:
        for board in boards:
            if not board.has_won():
                board.mark(i)
                if board.has_won():
                    last_winner_board = board
                    last_winner_move = i
    return last_winner_board, last_winner_move


if __name__ == "__main__":
    game = get_raw_input()
    winning_board, last_move = play_bingo(game)
    print(f"Found a winner after move {last_move}")
    print(f"Unmarked cells sum is {sum(winning_board.non_marked_cells())}")
    print(f"Final score is {sum(winning_board.non_marked_cells()) * last_move}")

    print()

    loser_board, last_winner_move = play_to_lose(game)
    print(f"Found loser after move {last_winner_move}")
    print(f"Unmarked cells sum is {sum(loser_board.non_marked_cells())}")
    print(f"Final score is {sum(loser_board.non_marked_cells()) * last_winner_move}")
