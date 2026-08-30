class Solution:
    def segregate0and1(self, arr):
        # code here
        left = 0
        right = len(arr) - 1

        while left < right:
            # Find 1 from the left
            while left < right and arr[left] == 0:
                left += 1

            # Find 0 from the right
            while left < right and arr[right] == 1:
                right -= 1

            # Swap
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        return arr
