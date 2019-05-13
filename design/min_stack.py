class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, x: int) -> None:
        self.arr.append(x)

    def pop(self) -> None:
        del self.arr[len(self.arr) - 1]

    def top(self) -> int:
        return self.arr[len(self.arr) - 1]

    def getMin(self) -> int:
        return sorted(self.arr)[0]

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