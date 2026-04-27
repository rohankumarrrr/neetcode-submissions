class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        # height : [1, 0, 2], output: 1
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        res = 0
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                res += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                res += right_max - height[right]
        return res
            


        