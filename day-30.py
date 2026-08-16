class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        while(n<=1):
            return n
        else:
            return self.nthFibonacci(n-1)+self.nthFibonacci(n-2)
