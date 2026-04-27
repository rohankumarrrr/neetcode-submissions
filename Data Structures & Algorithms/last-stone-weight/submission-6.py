class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxVal = max(stones)
        bucket = [0] * (maxVal + 1)
        for stone in stones:
            bucket[stone] += 1
        
        first = second = maxVal
        while first > 0:
            if bucket[first] >= 2:
                bucket[first] -= 2
                continue
            if bucket[first] == 0:
                first -= 1
                continue
            
            j = min(first - 1, second)
            while j > 0 and bucket[j] == 0:
                j -= 1
            if j == 0:
                return first
            
            second = j
            bucket[first] -= 1
            bucket[second] -= 1
            bucket[first - second] += 1
            first = max(first - second, second)
        
        return first