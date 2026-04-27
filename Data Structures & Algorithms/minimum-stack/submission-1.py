class MinStack:

    def __init__(self):
        self.stck = []
        self.min_stck = []

    def push(self, val: int) -> None:
        self.stck.append(val)
        self.min_stck.append(min(val, self.min_stck[-1] if self.min_stck else val))

    def pop(self) -> None:
        self.stck.pop()
        self.min_stck.pop()

    def top(self) -> int:
        return self.stck[-1]

    def getMin(self) -> int:
        return self.min_stck[-1]
