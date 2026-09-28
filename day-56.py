class Solution:
    def firstNonRepeating(self, arr):
        freq = {}

        # Count frequency of every element
        for x in arr:
            freq[x] = freq.get(x, 0) + 1

        # Find the first element whose frequency is 1
        for x in arr:
            if freq[x] == 1:
                return x

        return 0
