class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        new = []
        for num in nums:
            if num == val:
                continue
            new.append(num)
        
        for i, num in enumerate(new):
            nums[i] = num

        return len(new)