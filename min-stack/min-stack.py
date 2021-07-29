class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        
    def push(self, val: int) -> None:
        if not self.stack or val <= self.min[-1]:
            self.min.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]