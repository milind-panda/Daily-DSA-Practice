class Solution:
    def maxZeros(self, arr: list[list[int]]) -> int:
        n = len(arr)
        max_zeros = 0
        result = -1

        for j in range(n):       # Traverse columns
            count = 0

            for i in range(n):   # Traverse rows
                if arr[i][j] == 0:
                    count += 1

            if count > max_zeros:
                max_zeros = count
                result = j

        return result
