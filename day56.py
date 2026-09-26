class Solution:
    def countOccurence(self, arr, k):
        n = len(arr)

        freq = {}

        # Count frequencies
        for x in arr:
            freq[x] = freq.get(x, 0) + 1

        limit = n // k
        ans = 0

        # Count elements occurring more than n/k times
        for count in freq.values():
            if count > limit:
                ans += 1

        return ans
