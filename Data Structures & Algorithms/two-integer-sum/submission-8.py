class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}

        for i in range(len(nums)):
            cur = nums[i]
            if cur in targets:
                return [targets[cur], i]
            targets[target - cur] = i

        return []