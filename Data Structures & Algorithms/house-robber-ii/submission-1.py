class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        firstIgnore, secondIgnore = 0, nums[1]
        firstChoose, secondChoose = nums[0], max(nums[:2])
        for i in range(2, len(nums)):
            tmp = secondChoose
            secondChoose = max(secondChoose, nums[i] + firstChoose)
            firstChoose = tmp

            tmp = secondIgnore
            secondIgnore = max(secondIgnore, nums[i] + firstIgnore)
            firstIgnore = tmp
        
        return max(secondIgnore, firstChoose)