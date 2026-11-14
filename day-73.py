
class Solution:
    def sortedMatrix(self, mat):
        n = len(mat)

        # Step 1: Store all elements in a 1D list
        arr = []
        for i in range(n):
            for j in range(n):
                arr.append(mat[i][j])

        # Step 2: Sort the list
        arr.sort()

        # Step 3: Put elements back into the matrix
        k = 0
        for i in range(n):
            for j in range(n):
                mat[i][j] = arr[k]
                k += 1

        return mat
