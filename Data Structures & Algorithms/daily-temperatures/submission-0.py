class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = []
        prev_min = float("-inf")
        for i, t in enumerate(temperatures):
            while s and t > s[-1][0]:
                s_temp, s_idx = s.pop()
                res[s_idx] = i - s_idx
            s.append((t, i))    
        return res        