class Solution:
    def climbStairs(self, n: int) -> int:
        
        first, second = 1, 2

        for i in range(3, n + 1):
            first, second = second, first + second
        
        return second if n > 1 else first