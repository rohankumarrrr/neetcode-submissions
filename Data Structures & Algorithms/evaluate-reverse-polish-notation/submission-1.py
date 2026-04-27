class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stck = []
        for c in tokens:
            if c == '+':
                stck.append(stck.pop() + stck.pop())
            elif c == '*':
                stck.append(stck.pop() * stck.pop())
            elif c == '-':
                a, b = stck.pop(), stck.pop()
                stck.append(b - a)
            elif c == '/':
                a, b = stck.pop(), stck.pop()
                stck.append(int(float(b) / a))
            else:
                stck.append(int(c))
        return stck.pop()