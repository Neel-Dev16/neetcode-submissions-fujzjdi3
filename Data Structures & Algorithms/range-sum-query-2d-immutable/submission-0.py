class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.pref = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            rowSum = 0
            for c in range(cols):
                rowSum += matrix[r][c]
                self.pref[r + 1][c + 1] = self.pref[r][c + 1] + rowSum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row2 += 1
        col2 += 1
        return (self.pref[row2][col2] - self.pref[row1][col2]
                - self.pref[row2][col1] + self.pref[row1][col1])
