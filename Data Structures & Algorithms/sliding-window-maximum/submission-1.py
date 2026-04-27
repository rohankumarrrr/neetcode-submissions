from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l, r = 0, 0
        q = deque()

        output = []

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if q[0] < l:
                q.popleft()
            
            if k <= r + 1:
                output.append(nums[q[0]])
                l += 1
            r += 1
        
        return output