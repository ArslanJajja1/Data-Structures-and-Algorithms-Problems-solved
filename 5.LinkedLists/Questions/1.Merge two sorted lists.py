#21. Merge Two Sorted Lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #First Solution: Using extra space

        # dummy = ListNode()
        # curr = dummy
        # while l1 and l2:
        #     if l1.val <= l2.val:
        #         temp = ListNode(l1.val)
        #         l1 = l1.next
        #     else:
        #         temp = ListNode(l2.val)
        #         l2 = l2.next
        #     curr.next = temp
        #     curr = curr.next
        # while l1:
        #     temp = ListNode(l1.val)
        #     curr.next = temp
        #     curr = curr.next
        #     l1 = l1.next
        # while l2:
        #     temp = ListNode(l2.val)
        #     curr.next = temp
        #     curr = curr.next
        #     l2 = l2.next
        # return dummy.next

        # TC : O(N)
        # SC : O(N)

        # Second Approach : Without using extra space

        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                curr = l1
                l1 = l1.next
            else:
                curr.next = l2
                curr = l2
                l2 = l2.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next

        # TC : O(N)
        # SC : O(1)
    
        
        

            