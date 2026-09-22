class Solution:
    def countZeroes(self, arr):
        # code here
        count=0
        n=len(arr)
        for i in arr: 
            if i!=0:
                count+=1
        return n-count        
