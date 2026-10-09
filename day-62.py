
class Solution:
    def minAnd2ndMin(self, arr):
        first = float('inf')
        second = float('inf')

        for num in arr:
            if num < first:
                second = first
                first = num
            elif num < second and num != first:
                second = num

        if second == float('inf'):
            return [-1]

        return [first, second]
