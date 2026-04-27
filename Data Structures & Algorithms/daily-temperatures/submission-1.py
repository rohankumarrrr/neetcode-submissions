class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_idx, prev_temp = stack[-1]
                results[prev_idx] = idx - prev_idx
                stack.pop()
            stack.append((idx, temp))
        return results