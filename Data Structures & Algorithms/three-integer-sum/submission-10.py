class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if n > 0:
                return res
            if i > 0 and n == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if n + nums[l] + nums[r] > 0:
                    r -= 1
                elif n + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return res