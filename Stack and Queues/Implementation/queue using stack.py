# #! APPROACH ONE
# class Queue:
#     def __init__(self) -> None:
#         self.stack1 = []
#         self.stack2 = []

#     def push(self, value):
#         for i in range(len(self.stack1)):
#             self.stack2.append(self.stack1.pop())
#         self.stack1.append(value)
#         for i in range(len(self.stack2)):
#             self.stack1.append(self.stack2.pop())

#     def pop(self):
#         return self.stack1.pop()

#     def top(self):
#         print(self.stack1[-1])
#         return self.stack1[-1]

#     def printQueue(self):
#         for i in range(len(self.stack1)-1, -1, -1):
#             print(self.stack1[i], end=' ')


# q = Queue()
# q.push(2)
# q.push(4)
# q.push(6)
# q.pop()
# q.top()
# q.printQueue()

# #! APPROACH TWO
class Queue:
    def __init__(self) -> None:
        self.input = []
        self.output = []

    def push(self, value):
        self.input.append(value)

    def top(self):
        if self.output:
            return self.output[-1]
        else:
            for i in range(len(self.input)):
                self.output.append(self.input.pop())
            return self.output[-1]

    def pop(self):
        if self.output:
            return self.output.pop()
        else:
            for i in range(len(self.input)):
                self.output.append(self.input.pop())
            return self.output.pop()

    def printQueue(self):
        if self.output:
            for i in range(len(self.output)-1, -1, -1):
                print(self.output[i], end=' ')
        else:
            for i in range(len(self.input)):
                self.output.append(self.input.pop())
            for i in range(len(self.output)-1, -1, -1):
                print(self.output[i], end=' ')


q = Queue()
q.push(2)
q.push(4)
q.push(6)
q.push(8)


q.printQueue()
