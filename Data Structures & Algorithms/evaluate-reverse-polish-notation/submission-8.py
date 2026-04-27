class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        res = 0
        operators = {"+", "-", "*", "/"}
        for c in tokens:
            if c in operators:
                x = s.pop()
                y = s.pop()
                if c == "+":
                    s.append(x + y)
                elif c == "-":
                    s.append(y - x)
                elif c == "*":
                    s.append(x * y)
                else:
                    s.append(int(float(y) / x))
            else:
                s.append(int(c))
        return s[0]