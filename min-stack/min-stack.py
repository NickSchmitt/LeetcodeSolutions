from math import inf

class MinStack:

    def __init__(self):
        self.stack = []
        """
        initialize your data structure here.
        [1, 0]
        
        push 1, min is 1
        
        push 0, min is 0
        
        
        """
        

    def push(self, val: int) -> None:
        new_min = val if not self.stack else min(self.getMin(), val)
        self.stack.append((val, new_min))

    def pop(self) -> None:
        return self.stack.pop()[0]
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()