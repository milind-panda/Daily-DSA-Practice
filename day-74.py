
class Solution:
    def roundToNearest(self, s):
        last = int(s[-1])

        if last <= 5:
            return s[:-1] + '0'
        
        else:
            s = list(s)
            i = len(s) - 2

            while i >= 0 and s[i] == '9':
                s[i] = '0'
                i -= 1

            if i < 0:
                return '1' + '0' * len(s)

            s[i] = str(int(s[i]) + 1)

            return ''.join(s[:-1]) + '0'
