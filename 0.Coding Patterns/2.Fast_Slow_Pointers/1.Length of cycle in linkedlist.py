class ListNode:
    def __init__(self,val=0,next=None) -> None:
        self.val = val
        self.next = next
    
def length_of_cycle(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return calculate_length(slow)
    return 0
def calculate_length(slow):
    curr = slow.next
    cycle_length = 1
    while curr != slow:
        cycle_length += 1
        curr = curr.next
    return cycle_length

head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(5)
head.next.next.next = ListNode(7)
print(length_of_cycle(head))
head.next.next.next.next = head.next.next
print(length_of_cycle(head))

# TC : O(n)
# SC : O(1)