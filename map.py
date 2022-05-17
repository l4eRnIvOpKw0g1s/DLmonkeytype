class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val:int) -> None:
        self.stack.append(val)

    def pop(self):
        self.stack.pop()
        
    def top(self):
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)



obj = MinStack()
obj.push(4)
obj.push(3)
obj.push(9)
obj.push(1)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print (param_3, param_4)
print (obj.stack)