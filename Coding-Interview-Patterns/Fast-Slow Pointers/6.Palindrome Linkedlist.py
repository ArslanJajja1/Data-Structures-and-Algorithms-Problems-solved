# Palindrome LinkedList (medium) #
# Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

# Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. The algorithm should have O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

# Example 1:

# Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
# Output: true
# Example 2:

# Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
# Output: false

class ListNode:
    def __init__(self,value=0,next=None):
        self.value = value
        self.next = next

def find_palindrome(head):
    curr = head
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    slow_one = slow
    slow.next = reverse_linkedlist(slow.next)
    slow = slow.next
    while slow:
        if slow.value != curr.value:
            break
        curr = curr.next
        slow = slow.next
    slow_one.next = reverse_linkedlist(slow_one.next)
    return slow == None


def reverse_linkedlist(head):
    curr = head
    prev = None
    while curr:
        curr_next = curr.next
        curr.next = prev
        prev = curr
        curr = curr_next
    return prev

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(3)
head.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next = ListNode(1)

if(find_palindrome(head)):
    print('Linkedlist is palindrome')
else:
    print('Linkedlist is not palindrome')
