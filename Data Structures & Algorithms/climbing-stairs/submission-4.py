class Solution:
    def climbStairs(self, n: int) -> int:
        
        first, second = 0, 1
        for i in range(n):
            tmp = second
            first, second = second, first + tmp
        
        return second