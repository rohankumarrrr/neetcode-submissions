class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # memo[i] represents the minCost of traveling from steps 0...i inclusive
        first, second = cost[0], cost[1]
        for i in range(2, len(cost)):
            tmp = second
            second = cost[i] + min(first, second)
            first = tmp

        return min(first, second)
