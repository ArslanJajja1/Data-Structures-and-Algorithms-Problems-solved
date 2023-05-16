# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head_second_part = self.reverse(slow)
        head_first_part = head
        max_sum = 0
        
        while head_second_part:
            s = 0
            s = head_first_part.val + head_second_part.val
            max_sum = max(max_sum,s)
            head_first_part = head_first_part.next
            head_second_part = head_second_part.next
        return max_sum

    
    def reverse(self,head):
        prev = None
        while head:
            head_next = head.next
            head.next = prev
            prev = head
            head = head_next
        return prev
# TC : O(N)
# SC : O(1)