class Solution:
    def segregateElements(self, arr):
        # code here
        positive = []
        negative = []

        for x in arr:
            if x < 0:
                negative.append(x)
            else:
                positive.append(x)

        arr[:] = positive + negative
        return arr    
        
