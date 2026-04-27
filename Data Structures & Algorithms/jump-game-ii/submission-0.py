class Solution:
    def jump(self, nums: List[int]) -> int:
        
        minJumps = 0
        left, right = 0, 0
        
        while right < len(nums) - 1:
            farthestJumpIdx = 0
            for i in range(left, right + 1):
                farthestJumpIdx = max(farthestJumpIdx, i + nums[i])
            left = right + 1
            right = farthestJumpIdx
            minJumps += 1
        
        return minJumps
            
