# Problem Statement #
# Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

class ListNode:
    def __init__(self,value=0,next=None):
        self.value = value
        self.next = None

def find_start_of_cycle_first_approach(head):
    hashmap = {}
    while head:
        if head in hashmap:
            return head.value
        hashmap[head] = True
        head = head.next
    return None
    # Time Complexity : O(N)
    # Space Complexity : O(N)

def find_start_of_cycle_second_approach(head):
    slow = head
    slow_one = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            while True:
                slow = slow.next
                slow_one = slow_one.next
                if slow == slow_one:
                    return slow.value
    return None
    # Time Complexity : O(N)
    # Space Complexity : O(1)

def main():
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next.next = head.next.next
    # print(find_start_of_cycle_first_approach(head))
    print(find_start_of_cycle_second_approach(head))

main()
