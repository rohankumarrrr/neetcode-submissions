class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * (len(nums) + 1)
        for i, x in enumerate(nums):
            prefix[i + 1] = prefix[i] * nums[i]
        
        # [1, 2, 4, 6]
        # [1, 1, 2, 8, 48]
     #[1, 48, 24, 6, 1]

        postfix = [1] * (len(nums) + 1)
        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]
        
        prefix = prefix[:-1]
        postfix = postfix[1:]
        res = []

        for i in range(len(prefix)):
            res.append(prefix[i] * postfix[i])
        
        return res
