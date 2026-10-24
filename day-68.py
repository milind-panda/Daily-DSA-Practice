class Solution:
    def setBits(self, n):
        return bin(n).count('1')
