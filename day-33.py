class Solution:
    def thirdLargest(self, arr):
        if len(arr) < 3:
            return -1
        
        arr.sort(reverse=True)
        return arr[2]
      
