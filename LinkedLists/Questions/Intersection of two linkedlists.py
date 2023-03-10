# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        if not headA:
            return None
        if not headB:
            return None
        while a != b:
            a = headB if a == None else a.next
            b = headA if b == None else b.next
        return a