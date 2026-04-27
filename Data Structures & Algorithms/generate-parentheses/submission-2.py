class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pairs = []
        
        def generate(numOpen, numClosed, s):
            nonlocal pairs, n
            if numOpen == numClosed == n:
                pairs.append(s)
            if numOpen == numClosed and numOpen < n:
                generate(numOpen + 1, numClosed, s + "(")
            if numClosed < numOpen and numOpen == n:
                generate(numOpen, numClosed + 1, s + ")")
            if numClosed < numOpen and numOpen < n:
                generate(numOpen + 1, numClosed, s + "(")
                generate(numOpen, numClosed + 1, s + ")")
        
        generate(0, 0, "")
        return pairs