class Solution:
    def frequencyCount(self, arr):
        #  code here
        n = len(arr)
        freq = [0] * n

        for x in arr:
            freq[x - 1] += 1

        return freq
