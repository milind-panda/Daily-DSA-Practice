
class Solution:
    def minRow(self, mat):
        n = len(mat)

        min_count = float('inf')
        ans = 1

        for i in range(n):
            count = mat[i].count(1)

            if count < min_count:
                min_count = count
                ans = i + 1

        return ans
      
