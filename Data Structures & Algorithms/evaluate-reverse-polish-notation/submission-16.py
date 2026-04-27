class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for token in tokens:
            if not token in {"+", "-", "*", "/"}:
                stack.append(int(token))
                continue
            a, b = stack.pop(), stack.pop()
            if token == "+":
                stack.append(a + b)
            if token == "-":
                stack.append(b - a)
            if token == "*":
                stack.append(a * b)
            if token == "/":
                stack.append(int(float(b) / a))
        
        return stack[-1]