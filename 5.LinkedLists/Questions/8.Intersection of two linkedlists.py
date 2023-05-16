# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # First Approach

        # hashmap = {}
        # l1 = headA
        # l2 = headB
        # while l1:
        #     if l1 not in hashmap:
        #         hashmap[l1] = True
        #     l1 = l1.next
        # while l2:
        #     if l2 in hashmap:
        #         return l2
        #     l2 = l2.next
        # return None

        # TC : O(N)
        # SC : O(N)

        # Second Approach

        l1 = headA
        l2 = headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1

        # TC : O(N)
        # SC : O(1)


