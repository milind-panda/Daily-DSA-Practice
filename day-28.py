class Solution:
    def findElement(self, arr):
        # code here
        n=len(arr)
        right = [0] * n

        right[n - 1] = arr[n - 1]

        for i in range(n - 2, -1, -1):
            right[i] = min(arr[i], right[i + 1])

        max_left = arr[0]

        for i in range(1, n):
            if max_left <= arr[i] <= right[i]:
                return arr[i]

            max_left = max(max_left, arr[i])

        return -1
