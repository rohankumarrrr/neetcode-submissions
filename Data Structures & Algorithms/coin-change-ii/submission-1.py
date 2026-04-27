from collections import deque
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo = [0] * (amount + 1)
        memo[0] = 1
        
        for c in coins:
            for i in range(amount + 1):
                if i - c >= 0:
                    memo[i] += memo[i - c]
        
        return memo[amount]
            