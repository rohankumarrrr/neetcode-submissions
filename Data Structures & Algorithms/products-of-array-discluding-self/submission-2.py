class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 1, 2, 8, 48]
        # [48, 48, 24, 6, 1]
        prefix = 1
        prefix_sums = [prefix]
        for n in nums:
            prefix *= n
            prefix_sums.append(prefix)
        
        postfix = 1
        postfix_sums = [postfix]
        for n in nums[::-1]:
            postfix *= n
            postfix_sums.append(postfix)
        postfix_sums = postfix_sums[::-1]

        res = []
        for i in range(len(nums)):
            res.append(prefix_sums[i] * postfix_sums[i + 1])
        
        return res
        
