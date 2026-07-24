class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # monotonic stack
        # everytime we push a number to the stack, we compare to the top of the minStack. if it's smaller,
        # append that. if it's not smaller, append the top of the stack again. this way, we keep track
        #of the smallest number at each index.
        
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
