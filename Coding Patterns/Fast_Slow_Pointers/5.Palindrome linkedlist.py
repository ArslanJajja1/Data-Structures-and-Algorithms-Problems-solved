# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow = head
        fast = head
        curr = head
        # Find the middle of linkedlist
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the list from half
        temp = slow
        slow.next = self.reverse_list(slow.next)
        slow = slow.next
        while slow:
            if slow.val != curr.val:
                break
            slow = slow.next
            curr = curr.next
        temp.next = self.reverse_list(temp.next)
        if slow is None:
            return True
        return False


    def reverse_list(self,head):
        prev = None
        while head:
            head_next = head.next
            head.next = prev
            prev = head
            head = head_next
        return prev

# TC : O(N)
# SC : O(!)