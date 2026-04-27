class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n

        # memo = [0] * (n + 1)
        # memo[1], memo[2] = 1, 2
        memo = [1, 2]
        for i in range(3, n + 1):
            tmp = memo[1]
            memo[1] += memo[0]
            memo[0] = tmp
        
        return memo[1]
            