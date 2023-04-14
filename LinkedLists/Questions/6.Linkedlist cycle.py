# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # First Approach

        # hashmap = {}
        # curr = head
        # while curr:
        #     if curr not in hashmap:
        #         hashmap[curr] = True
        #     else:
        #         return True
        #     curr = curr.next
        # return False

        # TC : O(N)
        # SC : O(1)

        # Second Approach

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

        # TC : O(N)
        # SC : O(1)


