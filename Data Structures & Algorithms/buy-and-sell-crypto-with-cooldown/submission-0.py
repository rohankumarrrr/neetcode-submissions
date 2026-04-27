class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        visited = {}

        def dfs(i, bought):
            if i >= len(prices):
                return 0
            if (i, bought) in visited:
                return visited[(i, bought)]

            cooldown = dfs(i + 1, bought)
            if bought:
                visited[(i, bought)] = max(cooldown, dfs(i + 2, False) + prices[i])
            else:
                visited[(i, bought)] = max(cooldown, dfs(i + 1, True) - prices[i])
            
            return visited[(i, bought)]
        
        return dfs(0, False)
            