class Solution:
    def count(self, n):
        dp = [0] * (n + 1)
        
        dp[0] = 1
        
        for people in range(2, n + 1, 2):
            for left in range(0, people - 1, 2):
                right = people - left - 2
                dp[people] += dp[left] * dp[right]
        
        return dp[n]
      
