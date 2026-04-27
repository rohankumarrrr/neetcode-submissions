class Solution:
    def climbStairs(self, n: int) -> int:
        
        first, second = 1, 1
        for i in range(n - 1):
            tmp = second
            second += first
            first = tmp
        
        return second
            