# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        slow = head
        fast = head
        # Find middle of linked list
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head_second_half = self.reverse_list(slow.next)
        head_first_half = head
        while head_first_half and head_second_half:
            temp1 = head_first_half.next
            head_first_half.next = head_second_half
            head_first_half = temp1

            temp2 = head_second_half.next
            head_second_half.next = head_first_half
            head_second_half = temp2
        if head_first_half is not None:
            head_first_half.next = None
    def reverse_list(self,head):
        prev = None
        while head:
            head_next = head.next
            head.next = prev
            prev = head
            head = head_next
        return prev