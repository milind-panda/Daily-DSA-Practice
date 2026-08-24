class Solution:
    def minDist(self, arr, x, y):
        last_x = -1
        last_y = -1
        ans = float('inf')

        for i in range(len(arr)):
            if arr[i] == x:
                last_x = i

                if last_y != -1:
                    ans = min(ans, last_x - last_y)

            elif arr[i] == y:
                last_y = i

                if last_x != -1:
                    ans = min(ans, last_y - last_x)

        if ans == float('inf'):
            return -1

        return ans
    
