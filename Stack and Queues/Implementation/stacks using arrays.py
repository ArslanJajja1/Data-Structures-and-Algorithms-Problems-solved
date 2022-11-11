class Array:
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


arr1 = Array(6)
print(arr1.isEmpty())
arr1.push(1)
arr1.push(2)
arr1.push(3)
arr1.push(4)
arr1.push(5)
arr1.push(5)
print(arr1.isEmpty())
arr1.printStack()
print(arr1.pop())
print(arr1.pop())
print(arr1.topElement())
