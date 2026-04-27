class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        minProduct, maxProduct = 1, 1
        res = nums[0]
        for num in nums:
            tmp = maxProduct * num
            maxProduct = max(minProduct * num, maxProduct * num, num)
            minProduct = min(tmp, minProduct * num, num)
            res = max(res, maxProduct)
        
        return res