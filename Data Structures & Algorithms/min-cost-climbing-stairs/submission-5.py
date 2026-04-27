class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = [0] * len(cost)
        memo[0], memo[1] = cost[0], cost[1]

        first, second = cost[0], cost[1]

        for i in range(2, len(cost)):
            # memo[i] = min(memo[i - 1] + cost[i], memo[i - 2] + cost[i])
            tmp = second
            first, second = second, min(first + cost[i], second + cost[i])

        return min(first, second)
