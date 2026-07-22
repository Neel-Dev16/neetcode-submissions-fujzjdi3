class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.size = 0
        self.left = 0
        self.cap = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        right = (self.left + self.size) % self.cap
        self.q[right] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left = (self.left + 1) % self.cap
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.q[self.left]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.left + self.size - 1) % self.cap]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap
