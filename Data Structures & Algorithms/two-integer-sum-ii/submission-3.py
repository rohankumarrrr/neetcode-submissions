class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0, len(numbers) - 1):
            num = numbers[i]
            to_find = target - num
            if ((to_find in numbers[i + 1:None])):
                return [i + 1, numbers[i + 1:None].index(to_find) + i + 2]

        return [-1, -1]