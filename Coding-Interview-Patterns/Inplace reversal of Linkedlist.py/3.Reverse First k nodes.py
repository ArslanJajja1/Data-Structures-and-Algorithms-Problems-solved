# Problem 1: Reverse the first ‘k’ elements of a given LinkedList.

class ListNode:
    def __init__(self,value=0,next=None) -> None:
        self.value = value
        self.next = next
def print_linkedlist(head):
    while head:
        print(head.value)
        head = head.next
def reverse_first_k(head,k):
    dummy = ListNode()
    dummy.next = head
    prev = None
    head_prev = dummy
    curr = head
    for _ in range(k):
        curr_next = curr.next
        curr.next = prev
        prev = curr
        curr = curr_next

    head_prev.next.next = curr
    head_prev.next = prev
    print_linkedlist(dummy.next)
    return dummy.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next = ListNode(5)

reverse_first_k(head,3)


# Time Complexity : O(N)
# Space Complexity: O(1)