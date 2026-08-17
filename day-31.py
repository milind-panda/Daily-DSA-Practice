class Solution:
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:

        dp = [False] * (sum + 1)

        dp[0] = True

        for num in arr:
            for j in range(sum, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[sum]
