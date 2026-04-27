class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        # Input: nums = [2, 20, 4, 10, 3, 4, 5]
        # s = {2, 20, 4, 10, 3, 5}

        out = 0
        for n in s:
            if n - 1 not in s:
                # sequence begins here
                l = 0
                while n + l in s:
                    l += 1
                out = max(l, out)

        return out