class SudokuPuzzle:
    def __init__(self, puzzle: list[list]):
        self.puzzle = puzzle

    def print_puzzle(self):
        for row_num, row in enumerate(self.puzzle):
            if row_num % 3 == 0 and row_num != 0:
                line = "-"*6
                print(line+"+"+line+"-+"+line)
            for col_num, value in enumerate(row):
                if col_num % 3 == 0 and col_num != 0:
                    print("|", end=" ")
                if value == 0:
                    print(end="  ")
                else:
                    print(value, end=" ")
                if col_num == 8:
                    print()

    def complete(self) -> bool:
        row_sum = 1+2+3+4+5+6+7+8+9
        for row in self.puzzle:
            if sum(row) != row_sum:
                return False
        return True

    def open_cells(self) -> tuple:
        if self.complete():
            return []
        for row in range(9):
            for column in range(9):
                if self.puzzle[row][column] == 0:
                    yield row, column

    def row(self, r_num: int) -> set:
        assert 0 <= r_num <= 8, "Row out of bounds"
        return set(self.puzzle[r_num])

    def column(self, c_num: int) -> set:
        assert 0 <= c_num <= 8, "Column out of bounds"
        return set([self.puzzle[row][c_num] for row in range(9)])

    def block(self, r_num: int, c_num: int) -> set:
        assert 0 <= c_num <= 8, "Column out of bounds"
        assert 0 <= r_num <= 8, "Row out of bounds"
        block = set()

        row = r_num//3 * 3
        col = c_num//3 * 3

        for r in range(row, row+3):
            for c in range(col, col+3):
                block.add(self.puzzle[r][c])

        return block

    def __setitem__(self, pos, val):
        row, column = pos
        self.puzzle[row][column] = val

    def __getitem__(self, pos):
        row, column = pos
        return self.puzzle[row][column]
