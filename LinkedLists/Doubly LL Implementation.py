class ListNode:
    def __init__(self, value=0, next=None, previous=None) -> None:
        self.value = value
        self.next = next
        self.previous = previous


class LinkedList:
    def __init__(self, value) -> None:
        self.dummy = ListNode()
        self.head = ListNode(value)
        self.dummy.next = self.head
        self.head.previous = self.dummy
        self.tail = self.head
        self.length = 1
    # * O(1)

    def addAtEnd(self, value) -> None:
        newNode = ListNode(value)
        self.tail.next = newNode
        newNode.previous = self.tail
        self.tail = self.tail.next
        self.length += 1
    # * O(1)

    def removeFromEnd(self) -> None:
        previousNode = self.tail.previous
        previousNode.next = self.tail.next
        self.tail = previousNode
        self.length -= 1
    # *  O(1)

    def addAtStart(self, value) -> None:
        newNode = ListNode(value)
        self.dummy.next = newNode
        newNode.previous = self.dummy
        newNode.next = self.head
        self.head.previous = newNode
        self.head = newNode
        self.length += 1
    # * O(1)

    def removeFromStart(self) -> None:
        self.head = self.head.next
        self.dummy.next = self.head
        self.head.previous = self.dummy
        self.length -= 1
    # * O(1)

    def addAtIndex(self, index, value) -> None:
        temp = self.head
        iter = 0
        while iter != index-1:
            iter = iter+1
            temp = temp.next
        nextNode = temp.next
        newNode = ListNode(value)
        temp.next = newNode
        newNode.previous = temp
        newNode.next = nextNode
        nextNode.previous = newNode
        self.length += 1
    # * O(1)

    def removeAtIndex(self, index) -> None:
        temp = self.head
        iter = 0
        while iter != index-1:
            iter = iter+1
            temp = temp.next
        nodeToRemove = temp.next
        temp.next = nodeToRemove.next
        nodeToRemove.next.previous = temp
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
