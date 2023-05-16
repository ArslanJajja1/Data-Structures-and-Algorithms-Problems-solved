# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # First approach : by swaping node values

        # if not head or not head.next:
        #     return head
        # dummy = ListNode()
        # dummy.next = head
        # temp = head
        # while temp and temp.next:
        #     temp_val = temp.val
        #     temp.val = temp.next.val
        #     temp.next.val = temp_val
        #     temp = temp.next.next
        # return dummy.next

        # Second approach : 
        if not head or not head.next:
            return head
        dummy = ListNode()
        prev = dummy
        curr = head

        while curr and curr.next:
            second = curr.next
            nxt_pair = curr.next.next

            second.next = curr
            curr.next = nxt_pair
            prev.next = second

            prev = curr
            curr = curr.next
        return dummy.next

# TC : O(N)
# SC : O(1)