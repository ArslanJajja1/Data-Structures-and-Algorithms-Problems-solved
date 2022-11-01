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


ll = LinkedList(2)
ll.addAtEnd(4)
ll.addAtEnd(5)
ll.addAtEnd(6)
ll.addAtEnd(7)
# ll.printLinkedList()
# ll.removeFromEnd()
# ll.printLinkedList()
ll.addAtStart(8)
# ll.printLinkedList()
# ll.removeFromStart()
# ll.printLinkedList()
ll.addAtIndex(2, 9)
# ll.printLinkedList()
ll.removeAtIndex(3)
ll.printLinkedList()
