class Solution:
    def maxValue(self, arr):
        arr.sort()

        ans = 0
        MOD = 10**9 + 7

        for i in range(len(arr)):
            ans = (ans + arr[i] * i) % MOD

        return ans
