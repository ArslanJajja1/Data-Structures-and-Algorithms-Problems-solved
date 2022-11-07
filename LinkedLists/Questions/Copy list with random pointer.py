"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        res = temp
        while temp:
            front = temp.next
            copyNode = Node(temp.val)
            temp.next = copyNode
            copyNode.next = front
            temp = front
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next
        temp = head
        dummy = Node(0)
        copyList = dummy
        while temp:
            front = temp.next.next
            copyList.next = temp.next
            temp.next = front
            copyList = copyList.next
            temp = temp.next
        return dummy.next
