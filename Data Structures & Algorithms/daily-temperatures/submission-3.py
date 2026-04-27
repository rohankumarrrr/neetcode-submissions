class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        results = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                results[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append((i, temp))
        
        return results
