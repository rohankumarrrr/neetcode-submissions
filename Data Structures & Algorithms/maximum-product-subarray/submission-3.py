class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]
        maxProduct, minProduct = 1, 1

        for num in nums:
            minProduct, maxProduct = min(minProduct * num, maxProduct * num, num), max(maxProduct * num, minProduct * num, num)
            res = max(res, maxProduct)
        
        return res