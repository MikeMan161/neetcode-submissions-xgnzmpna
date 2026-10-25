class MinStack:
    def __init__(self):
        self.stack=[]
        self.minStack=[]
        

    def push(self, val: int) -> None:
        if self.minStack and val > self.minStack[-1]:
            self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)
        self.stack.append(val)

        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return int(self.stack[-1])
        

    def getMin(self) -> int:
        return int(self.minStack[-1])
