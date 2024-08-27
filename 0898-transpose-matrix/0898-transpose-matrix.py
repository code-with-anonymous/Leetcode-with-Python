from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        a = []

        # Initialize the transposed matrix with zeros
        zero = [0] * row
        for i in range(col):  # Should iterate over columns, not rows
            a.append(zero.copy())

        # Fill in the transposed values
        for r in range(row):  # Should iterate over rows, not columns
            for c in range(col):
                a[c][r] = matrix[r][c]  # Correct the indices for transposing

        return a
