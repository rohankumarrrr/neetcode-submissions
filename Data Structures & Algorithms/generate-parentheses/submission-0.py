class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stck = []
        output = []

        def recurse(num_open, num_closed):
            if num_open == num_closed == n:
                s = "".join(stck)
                output.append(s)
            if num_open < n:
                stck.append("(")
                recurse(num_open + 1, num_closed)
                stck.pop()
            if num_closed < num_open:
                stck.append(")")
                recurse(num_open, num_closed + 1)
                stck.pop()
        
        recurse(0, 0)
        return output
