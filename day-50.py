class Solution:
    def recursiveSum(self, n):
        # Base case
        if n == 0:
            return 0
        
        # Recursive case
        return n + self.recursiveSum(n - 1)
