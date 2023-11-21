# Problem Statement #
# Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.

class ListNode:
    def __init__(self,value=0,next=None) -> None:
        self.value = value
        self.next = next
def print_linkedlist(head):
    while head:
        print(head.value)
        head = head.next
def reverse_sublist(head, p, q):
    if p == q:
        return head  # No change needed if p and q are the same.

    dummy = ListNode(0)
    dummy.next = head
    p_prev = dummy

    for _ in range(p - 1):
        p_prev = p_prev.next

    p_node = p_prev.next
    prev = None

    for _ in range(q - p + 1):
        next_node = p_node.next
        p_node.next = prev
        prev = p_node
        p_node = next_node

    p_prev.next.next = p_node
    p_prev.next = prev

    return dummy.next

        


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(6)
# head.next.next.next.next.next.next = ListNode(7)
reverse_sublist(head,2,4)
print_linkedlist(head)


# Time Complexity : O(N)
# Space Complexity: O(1)