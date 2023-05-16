class Stack:
    def __init__(self, size) -> None:
        self.arr = [None]*size
        self.top = -1
        self.size = size

    def push(self, val):
        if self.top == self.size:
            return 'No space available'
        self.top += 1
        print('top', self.top)
        self.arr[self.top] = val

    def pop(self):
        if self.top == -1:
            return
        num = self.arr[self.top]
        self.top -= 1
        return num

    def topElement(self):
        return self.arr[self.top]

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def printStack(self):
        print(self.arr)
        for i in range(self.size):
            print(self.arr[i])


stack1 = Stack(6)
print(stack1.isEmpty())
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)
stack1.push(5)
print(stack1.isEmpty())
stack1.printStack()
print(stack1.pop())
print(stack1.pop())
print(stack1.topElement())
