class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left, right = 0, k
        output = []
        while (right != len(nums) + 1):
            sub_nums = sorted(nums[left:right], reverse=True)
            output.append(sub_nums[0])
            left += 1
            right += 1
        return output