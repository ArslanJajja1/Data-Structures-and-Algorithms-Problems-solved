# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
       # First approach

        # if not head or not head.next:
        #     return head
        # curr = head
        # length = 0
        # while curr:
        #    curr = curr.next
        #    length += 1
        # index = length // 2
        # count = 0
        # while head:
        #     head = head.next
        #     count += 1
        #     if count == index:
        #         return head
        # return None

        # Second approach : 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

        # TC : O(N)
        # SC : O(1)