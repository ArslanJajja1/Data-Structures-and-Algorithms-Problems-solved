class Queue:
    def __init__(self, size) -> None:
        self.queue = []
        self.front = 0
        self.rear = 0
        self.size = size
        self.count = 0

    def enqueue(self, val):
        if self.rear == self.size:
            return -1
        self.queue.append(val)
        self.rear += 1

    def dequeue(self):
        if self.front == self.rear:
            return -1
        popItem = self.queue.pop(0)
        self.rear -= 1
        return popItem

    def peek(self):
        return self.queue[self.front]

    def printQueue(self):
        for i in self.queue:
            print(i, end=' ')


arr1 = Queue(5)
arr1.enqueue(2)
arr1.enqueue(4)
arr1.enqueue(6)
arr1.enqueue(8)
arr1.dequeue()
print(arr1.peek())
arr1.printQueue()
