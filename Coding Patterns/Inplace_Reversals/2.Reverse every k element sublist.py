# Reverse every k element sublist
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverse_every_k_element(head,k):
    previous = None
    curr = head
    while True:
        last_node_of_previous_part = previous
        last_node_of_sublist = curr
        next = None
        i = 0
        while curr is not None and i < k:
            next = curr.next
            curr.next = previous
            previous = curr
            curr = next
            i += 1
        if last_node_of_previous_part is not None:
            last_node_of_previous_part.next = previous
        else:
            head = previous
        last_node_of_sublist.next = curr
        if curr is None:
            break
        previous = last_node_of_sublist
    return head



head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next.next = ListNode(8)
print(reverse_every_k_element(head,3))


