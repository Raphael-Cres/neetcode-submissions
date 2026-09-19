class Solution:
    def climbStairs(self, n: int) -> int:
        x0 = 1
        x1 = 2
        if n ==1:
            return 1
            
        S = 3
        for i in range (3,n+1):
            S += x0 + x1
            x0,x1 = x1, x0+x1

        return x1

        