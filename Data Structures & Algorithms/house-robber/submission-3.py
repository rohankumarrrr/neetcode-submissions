class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        first, second = nums[0], max(nums[0:2])
        for i in range(2, len(nums)):
            tmp = second
            second = max(nums[i] + first, second)
            first = tmp

        return second