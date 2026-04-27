class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        new_list = sorted(self.nums, reverse=True)
        return new_list[self.k - 1]
