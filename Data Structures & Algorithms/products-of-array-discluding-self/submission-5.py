class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * (len(nums) + 1)

        # [1,2,4,6]
        # [1, 1, 2, 8, 48]
        # [48, 48, 24, 6, 1]

        for i in range(len(nums)):
            output[i + 1] = nums[i] * output[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output[:-1]
