class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pairs = []
        stack = []
        def generate(numOpen, numClosed):
            if numOpen == numClosed == n:
                pairs.append(''.join(stack))
            if numOpen == numClosed and numOpen < n:
                stack.append('(')
                generate(numOpen + 1, numClosed)
                stack.pop()
            if numClosed < numOpen and numOpen == n:
                stack.append(')')
                generate(numOpen, numClosed + 1)
                stack.pop()
            if numClosed < numOpen and numOpen < n:
                stack.append('(')
                generate(numOpen + 1, numClosed)
                stack.pop()
                stack.append(')')
                generate(numOpen, numClosed + 1)
                stack.pop()
        
        generate(0, 0)
        return pairs