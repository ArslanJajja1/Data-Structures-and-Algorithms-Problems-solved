from email import header


class ListNode:
    def __init__(self, value=0, next=None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, value) -> None:
        self.dummy = ListNode()
        self.head = ListNode(value)
        self.dummy.next = self.head
        self.tail = self.head
        self.length = 1
    # * O(1)

    def addAtEnd(self, value) -> None:
        self.tail.next = ListNode(value)
        self.tail = self.tail.next
        self.length += 1
    # * O(1)

    def removeFromEnd(self) -> None:
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
        temp.next = None
        self.tail = temp
        self.length -= 1
    # *  O(1)

    def addAtStart(self, value) -> None:
        self.dummy.next = ListNode(value)
        self.dummy.next.next = self.head
        self.head = self.dummy.next
        self.length += 1
    # * O(1)

    def removeFromStart(self) -> None:
        self.head = self.head.next
        self.dummy.next = self.head
        self.length -= 1
    # * O(1)

    def addAtIndex(self, index, value) -> None:
        temp = self.head
        iter = 0
        while iter != index-1:
            iter = iter+1
            temp = temp.next
        nextNode = temp.next
        temp.next = ListNode(value)
        temp.next.next = nextNode
        self.length += 1
    # * O(1)

    def removeAtIndex(self, index) -> None:
        temp = self.head
        iter = 0
        while iter != index-1:
            iter = iter+1
            temp = temp.next
        temp.next = temp.next.next
        self.length -= 1
    # * O(n)

    def printLinkedList(self) -> None:
        temp = self.head
        iter = 0
        print('Length :', self.length)
        while temp:
            print('Index ',
                  iter, ':', temp.value, end=', ')
            temp = temp.next
            iter += 1
    # * Reverse a linked list iteratively

    def reverseLlIteratively(self):
        prev = None
        if not self.head:
            return prev
        while self.head:
            nextNode = self.head.next
            self.head.next = prev
            prev = self.head
            self.head = nextNode
        self.head = prev
        return prev

    def reverseListRecursively(self, head, prev=None):
        if not head:
            return prev
        nextNode = head.next
        head.next = prev
        return self.reverseListRecursively(nextNode, head)

    def removeNthNodeFromEnd(self, n):
        slow = self.head
        fast = self.head
        for i in range(0, n):
            if not fast.next:
                if i == n-1:
                    head = head.next
                return head
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        if slow.next:
            slow.next = slow.next.next
        return self.head

    def middleOfLinkedList1(self):
        curr = self.head
        length = 0
        while curr:
            curr = curr.next
            length = length+1
        index = length//2
        count = 0
        temp = self.head
        while count != index:
            temp = temp.next
            count = count+1
        return temp

    def middleOfLinkedList2(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


ll = LinkedList(2)
ll.addAtEnd(4)
ll.addAtEnd(6)
ll.addAtEnd(8)
ll.addAtEnd(9)
ll.addAtEnd(10)
ll.addAtEnd(11)
ll.addAtEnd(12)
ll.addAtEnd(13)
ll.addAtEnd(14)
print(ll.middleOfLinkedList1().value)
print(ll.middleOfLinkedList2().value)
