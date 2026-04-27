class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        subset = []
        def build_powerset(i: int):
            if i >= len(nums):
                output.append(subset.copy())
                return
            
            subset.append(nums[i])
            build_powerset(i + 1)

            subset.pop()
            build_powerset(i + 1)
        
        build_powerset(0)
        return output
        