class Solution:
    def kthElement(self, a, b, k):
        # code here
        n = len(a)
        m = len(b)

        # Always binary search on the smaller array
        if n > m:
            return self.kthElement(b, a, k)

        # Number of elements taken from a
        low = max(0, k - m)
        high = min(k, n)

        while low <= high:
            cutA = (low + high) // 2
            cutB = k - cutA

            # Left side values
            leftA = a[cutA - 1] if cutA > 0 else float('-inf')
            leftB = b[cutB - 1] if cutB > 0 else float('-inf')

            # Right side values
            rightA = a[cutA] if cutA < n else float('inf')
            rightB = b[cutB] if cutB < m else float('inf')

            # Correct partition
            if leftA <= rightB and leftB <= rightA:
                return max(leftA, leftB)

            # Too many elements taken from a
            elif leftA > rightB:
                high = cutA - 1

            # Too few elements taken from a
            else:
                low = cutA + 1

        return -1
