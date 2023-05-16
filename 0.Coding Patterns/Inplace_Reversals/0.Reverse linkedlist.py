# 206. Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode],prev=None) -> Optional[ListNode]:
        # prev=None
        # if not head:
        #    return prev
        # while head:
        #     nextNode=head.next
        #     head.next=prev
        #     prev=head
        #     head=nextNode
        # return prev
# TC : O(N)
# SC : O(1)
        # if not head:
        #     return prev
        # nextNode=head.next
        # head.next=prev
        # return self.reverseList(nextNode,head)

        # Recursive way
        if not head:
            return None
        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return new_head
