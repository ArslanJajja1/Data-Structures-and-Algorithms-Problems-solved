# Problem Statement #
# Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the reversed LinkedList.

class ListNode:
    def __init__(self,value=0,next=None):
        self.value = value
        self.next = next
def print_linkedlist(head):
    while head:
        print(head.value)
        head = head.next

def reverse_linkedlist(head):
    prev = None
    curr = head
    while curr:
        curr_next = curr.next
        curr.next = prev
        prev = curr
        curr = curr_next
    print_linkedlist(prev)
    return prev
def reverse_linkedlist_recursively(curr,prev=None):
    if curr is None:
        print_linkedlist(prev)
        return prev
    curr_next = curr.next
    curr.next = prev
    reverse_linkedlist_recursively(curr_next,curr)


head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
reverse_linkedlist(head)
# reverse_linkedlist_recursively(head)

# Time Complexity : O(N)
# Space Complexity: O(1)


