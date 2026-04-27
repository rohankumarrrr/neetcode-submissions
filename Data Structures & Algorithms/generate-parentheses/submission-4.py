class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def generate(numOpen, numClosed):
            if numOpen == numClosed == n:
                res.append(''.join(stack))
                return
            if numClosed < numOpen:
                stack.append(')')
                generate(numOpen, numClosed + 1)
                stack.pop()
            if numOpen < n:
                stack.append('(')
                generate(numOpen + 1, numClosed)
                stack.pop()
        
        generate(0, 0)
        return res
            