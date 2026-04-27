class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, x in enumerate(nums):
            if x in hash_map.keys():
                return [hash_map[x], i]
            else:
                hash_map[target - x] = i
        return []


        
            