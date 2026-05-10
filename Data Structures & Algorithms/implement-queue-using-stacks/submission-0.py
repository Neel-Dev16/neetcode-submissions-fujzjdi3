class MyQueue:

    def __init__(self):
        self.InputStack=[]
        self.OutputStack=[]
    def push(self, x: int) -> None:
        self.InputStack.append(x)        
    def pop(self) -> int:
        self.move()
        return self.OutputStack.pop()
    def peek(self) -> int:
        self.move()
        return self.OutputStack[-1]
    def empty(self) -> bool:
        return not self.InputStack and not self.OutputStack
    def move(self)->None:
        if not self.OutputStack:
            while self.InputStack:
                self.OutputStack.append(self.InputStack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()