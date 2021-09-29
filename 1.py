class Stack:
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        return self.stack == []
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data
    def peek(self):
        return self.stcak[-1]
    def stackSize(self):
        return len(self.stack)


s = Stack()
s.push(1)
s.push(10)
s.push(100)
s.push(1000)
print(s.stackSize())
print("Popped element is:",s.pop())
print("Stack size after popping is:",s.stackSize())
print(s)
