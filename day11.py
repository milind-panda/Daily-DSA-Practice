class Solution:
    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low

        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[high] = arr[high], arr[i]
        return i

    def quickSelect(self, arr, low, high, k):
        if low <= high:
            p = self.partition(arr, low, high)

            if p == k:
                return arr[p]
            elif p > k:
                return self.quickSelect(arr, low, p - 1, k)
            else:
                return self.quickSelect(arr, p + 1, high, k)

    def kthSmallest(self, arr, k):
        return self.quickSelect(arr, 0, len(arr) - 1, k - 1)
