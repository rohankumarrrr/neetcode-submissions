class MinStack:

    def __init__(self):
        self.s = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.s.append(val)
        x = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(x)

    def pop(self) -> None:
        self.s.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

        
