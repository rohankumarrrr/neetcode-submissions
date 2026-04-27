class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # memo[i] represents the minCost of traveling from steps 0...i inclusive
        memo = [0] * len(cost)
        memo[0], memo[1] = cost[0], cost[1]

        for i in range(2, len(cost)):
            memo[i] = cost[i] + min(memo[i - 1], memo[i - 2])

        return min(memo[-2], memo[-1])
