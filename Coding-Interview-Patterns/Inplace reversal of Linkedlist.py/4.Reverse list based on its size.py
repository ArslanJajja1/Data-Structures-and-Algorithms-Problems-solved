class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
def print_linkedlist(head):
    while head:
        print(head.value)
        head = head.next
def reverse_linkedlist(head, p, q):
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

def reverse_list_based_size(head):
    size = 0
    curr = head
    while curr:
        size += 1
        curr = curr.next

    if size % 2 == 0:
        head = reverse_linkedlist(head, 1, size // 2)
        head = reverse_linkedlist(head, size // 2 + 1, size)
    else:
        head = reverse_linkedlist(head, 1, size // 2)
        # Skip the middle element by starting from size // 2 + 2
        head = reverse_linkedlist(head, size // 2 + 2, size)
    print_linkedlist(head)
    return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

reverse_list_based_size(head)
