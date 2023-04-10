# middle of linkedlist
class ListNode:
    def __init__(self,val=0,next=None) -> None:
        self.val = val
        self.next = next

def middle_of_ll(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
print(middle_of_ll(head))

# TC : O(N)
# SC : O(1)