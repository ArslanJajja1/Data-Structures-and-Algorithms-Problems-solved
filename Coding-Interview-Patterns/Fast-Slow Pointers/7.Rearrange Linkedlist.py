# Rearrange a LinkedList (medium) #
# Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order. So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

# Your algorithm should not use any extra space and the input LinkedList should be modified in-place.

# Example 1:

# Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
# Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null 
# Example 2:

# Input: 2 -> 4 -> 6 -> 8 -> 10 -> null
# Output: 2 -> 10 -> 4 -> 8 -> 6 -> null

class ListNode:
    def __init__(self,value=0,next=None):
        self.value = value
        self.next = next

def rearrange_linkedlist(head):
    curr = head
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    head_first_half = head
    head_second_half = reverse_linkedlist(slow.next)

    while head_second_half:
        head_next = head_first_half.next
        head_first_half.next = head_second_half
        head_first_half = head_next

        head_next = head_second_half.next
        head_second_half.next = head_first_half
        head_second_half = head_next
    if head_first_half is not None:
        head_first_half.next = None
    print_linkedlist(head)
    return head

def print_linkedlist(head):
    curr = head
    while curr:
        print(curr.value)
        curr = curr.next

def reverse_linkedlist(head):
    curr = head
    prev = None
    while curr:
        curr_next = curr.next
        curr.next = prev
        prev = curr
        curr = curr_next
    return prev

head = ListNode(2)
head.next = ListNode(4)
head.next.next = ListNode(6)
head.next.next.next = ListNode(8)
head.next.next.next.next = ListNode(10)
head.next.next.next.next.next = ListNode(12)
print(rearrange_linkedlist(head))

# Time Complexity : O(N)
# Space Complexity : O(1)