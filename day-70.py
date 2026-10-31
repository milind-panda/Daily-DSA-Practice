
class Solution:
    def sequence(self, n):
        MOD = 10**9 + 7

        ans = 0
        num = 1

        for i in range(1, n + 1):
            product = 1

            for j in range(i):
                product = (product * num) % MOD
                num += 1

            ans = (ans + product) % MOD

        return ans
