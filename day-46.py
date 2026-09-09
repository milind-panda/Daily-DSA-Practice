class Solution:
    def minimumInteger(self, arr):
        n = len(arr)
        s = sum(arr)

        # Ceiling of average
        required = (s + n - 1) // n

        # Smallest element >= required
        ans = float('inf')

        for x in arr:
            if x >= required:
                ans = min(ans, x)

        return ans
