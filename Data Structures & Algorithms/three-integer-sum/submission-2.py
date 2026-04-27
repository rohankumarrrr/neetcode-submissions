class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i in range(len(nums)):
            x = nums[i]
            if x > 0:
                break
            if i != 0 and x == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            print(str(i) + " " + str(left) + " " + str(right))
            while (left < right):
                total = x + nums[left] + nums[right]
                if (total == 0):
                    output.append([x, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif (total > 0):
                    right -= 1
                elif (total < 0):
                    left += 1
        
        return output