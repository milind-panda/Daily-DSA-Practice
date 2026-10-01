class Solution:
    def intersectSize(self, a, b):
        s = set(a)
        count = 0

        for x in b:
            if x in s:
                count += 1

        return count
