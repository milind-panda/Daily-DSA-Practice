class Solution:    
    def findUnion(self, a, b):
        # code here
        union = set()

        for x in a:
            union.add(x)

        for x in b:
            union.add(x)

        return list(union)
