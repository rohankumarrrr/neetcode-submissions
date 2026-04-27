class DynamicArray:
    
    def __init__(self, capacity: int):
        self.store = []
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.store[i]

    def set(self, i: int, n: int) -> None:
        self.store[i] = n

    def pushback(self, n: int) -> None:
        self.store.append(n)
        if len(self.store) > self.capacity:
            self.capacity *= 2

    def popback(self) -> int:
        out = self.store[-1]
        self.store.pop()
        return out

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return len(self.store)
    
    def getCapacity(self) -> int:
        return self.capacity