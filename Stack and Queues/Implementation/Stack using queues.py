# #! FIRST APPROACH
# class Stack:
#     def __init__(self) -> None:
#         self.queue1 = []
#         self.queue2 = []

#     def push(self, value):
#         # add value in queue 2
#         self.queue2.append(value)
#         # add queue 1 values in queue 2
#         for i in range(0, len(self.queue1)):
#             item = self.queue1.pop(0)
#             self.queue2.append(item)
#         # swap queue 1 and queue 2
#         for i in range(0, len(self.queue2)):
#             item = self.queue2.pop(0)
#             self.queue1.append(item)

#     def pop(self):
#         self.queue1.pop(0)

#     def printStack(self):
#         for i in self.queue1:
#             print(i, end=' ')


# stack1 = Stack()
# stack1.push(2)
# stack1.push(4)
# stack1.push(6)
# stack1.push(8)
# stack1.pop()
# stack1.printStack()

# #! SECOND APPROACH

class Stack:
    def __init__(self) -> None:
        self.queue = []

    def push(self, value):
        self.queue.append(value)
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.pop(0))

    def pop(self):
        return self.queue.pop(0)

    def top(self):
        return self.queue[0]

    def printStack(self):
        for i in self.queue:
            print(i, end=" ")


st = Stack()
st.push(3)
st.push(5)
st.push(7)
st.push(9)
st.pop()
st.printStack()
