class Solution:
    def firstElementKTime(self, arr, k):
        freq = {}

        for x in arr:
            freq[x] = freq.get(x, 0) + 1

            if freq[x] >= k:
                return x

        return -1
