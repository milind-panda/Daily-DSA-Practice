class Solution:
    def isSubset(self, a, b):
        # code here
        freq = {}

        # Count frequency of elements in a
        for x in a:
            freq[x] = freq.get(x, 0) + 1

        # Check elements of b
        for x in b:
            if x not in freq or freq[x] == 0:
                return False

            freq[x] -= 1

        return True
