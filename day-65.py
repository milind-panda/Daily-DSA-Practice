
class Solution:
    def checkPangram(self, s):
        # code here
        s = s.lower()

        letters = set()

        for ch in s:
            if 'a' <= ch <= 'z':
                letters.add(ch)

        return len(letters) == 26
