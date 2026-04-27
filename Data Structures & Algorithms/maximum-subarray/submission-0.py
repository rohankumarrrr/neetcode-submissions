class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if all(x < 0 for x in nums):
            return max(nums)
        
        currSum = 0
        maxSum = 0

        for x in nums:
            if currSum + x < 0:
                currSum = 0
            else:
                currSum += x
            maxSum = max(maxSum, currSum)
        
        return maxSum

    