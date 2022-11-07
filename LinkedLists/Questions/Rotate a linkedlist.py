# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or not k:
            return head
        length = 1
        temp = head
        while temp.next:
            length = length+1
            temp = temp.next
        temp.next = head
        k = k % length
        k = length-k
        while temp and k > 0:
            temp = temp.next
            k = k-1
        head = temp.next
        temp.next = None
        return head
