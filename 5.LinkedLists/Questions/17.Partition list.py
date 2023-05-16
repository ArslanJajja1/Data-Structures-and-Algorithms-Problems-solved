# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = left_ptr = ListNode()
        dummy2 = right_ptr = ListNode()
        curr = head
        while curr:
            if curr.val < x:
                left_ptr.next = curr
                left_ptr = left_ptr.next
            else:
                right_ptr.next = curr
                right_ptr = right_ptr.next
            curr = curr.next
        right_ptr.next = None
        left_ptr.next = dummy2.next
        return dummy1.next

# TC : O(N)
# SC : O(1)
        