# Start of a linkedlist
class ListNode:
    def __init__(self,val=0,next=None) -> None:
        self.val = val
        self.next = next
def find_start_of_ll(head):
        if not head or not head.next:
           return None
        hashmap = {}
        curr = head
        while curr != None:
            if curr not in hashmap:
                hashmap[curr] = True
            else:
                return curr.val
            curr = curr.next
        return None

head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(5)
head.next.next.next = ListNode(7)
print(find_start_of_ll(head))
head.next.next.next.next = head.next.next
print(find_start_of_ll(head))

# TC : O(N)
# SC : O(N)