class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
class MyCircularQueue:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.size = k
        self.length = 0
    def enQueue(self, value: int) -> bool:
        if self.length == self.size:
            return False
        node = ListNode(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.length += 1
        return True
    def deQueue(self) -> bool:
        if self.length == 0:
            return False
        self.head = self.head.next
        self.length -= 1
        return True
    def Front(self) -> int:
        if self.length == 0:
            return -1
        return self.head.val
    def Rear(self) -> int:
        if self.length == 0:
            return -1
        return self.tail.val
    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.size

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()