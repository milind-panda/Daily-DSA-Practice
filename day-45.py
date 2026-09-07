class Solution:
    def addOne(self, arr):
        n = len(arr)

        # Start from the last digit
        for i in range(n - 1, -1, -1):

            if arr[i] < 9:
                arr[i] += 1
                return arr

            # Current digit is 9, so make it 0
            arr[i] = 0

        # If all digits were 9
        return [1] + arr
