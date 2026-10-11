class Solution:
    def boundaryTraversal(self, mat):
        n = len(mat)
        m = len(mat[0])
        res = []

        # Single row: just the row
        if n == 1:
            return mat[0][:]

        # Single column: just the column top to bottom
        if m == 1:
            return [mat[i][0] for i in range(n)]

        # Top row, left to right
        for j in range(m):
            res.append(mat[0][j])

        # Right column, top to bottom (excluding the top-right corner)
        for i in range(1, n):
            res.append(mat[i][m - 1])

        # Bottom row, right to left (excluding the bottom-right corner)
        for j in range(m - 2, -1, -1):
            res.append(mat[n - 1][j])

        # Left column, bottom to top (excluding both left corners)
        for i in range(n - 2, 0, -1):
            res.append(mat[i][0])

        return res
