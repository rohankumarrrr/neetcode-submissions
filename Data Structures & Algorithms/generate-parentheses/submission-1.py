class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = []
        
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(s))
                return
            if openN < n:
                s.append("(")
                backtrack(openN + 1, closedN)
                s.pop()
            if closedN < openN:
                s.append(")")
                backtrack(openN, closedN + 1)
                s.pop()
        
        backtrack(0, 0)
        return res