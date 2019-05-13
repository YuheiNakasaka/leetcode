class MinStack:

    def __init__(self):
        self.arr = []
        self.min = []

    def push(self, x: int) -> None:
        self.arr.append(x)
        if not len(self.min):
            self.min.append(x)
        elif x <= self.min[-1]:
            self.min.append(x)

    def pop(self) -> None:
        if self.arr.pop() == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print('Success') if obj.getMin() == -3 else print(obj.getMin())
obj.pop()
print('Success') if obj.top() == 0 else print(obj.top())
print('Success') if obj.getMin() == -2 else print(obj.getMin())