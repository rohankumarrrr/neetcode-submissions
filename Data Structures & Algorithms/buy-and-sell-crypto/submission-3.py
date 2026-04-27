class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l, r = 0, 1
        while r < len(prices):
            p = prices[r] - prices[l]
            maxProfit = max(maxProfit, p)
            if p < 0:
                l = r
            r += 1
        
        return maxProfit