class Solution:
    def firstRepeated(self, arr):
        freq = {}

        for x in arr:
            freq[x] = freq.get(x, 0) + 1

        for i in range(len(arr)):
            if freq[arr[i]] > 1:
                return i + 1

        return -1
        
