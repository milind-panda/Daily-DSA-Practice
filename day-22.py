class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        if len(a) != len(b):
            return False

        a.sort()
        b.sort()

        return a == b       
