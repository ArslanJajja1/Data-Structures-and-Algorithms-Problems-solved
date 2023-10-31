# Problem Statement #
# Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

# If the total number of nodes in the LinkedList is even, return the second middle node.

# Example 1:

# Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
# Output: 3
# Example 2:

# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
# Output: 4
# Example 3:

# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
# Output: 4

class ListNode:
    def __init__(self,value=0,next=None):
        self.value = value
        self.next = next

def find_middle_of_linkedlist_first_approach(head):
    curr = head
    length = 0
    while curr:
        length += 1
        curr = curr.next
    index_to_find = (length//2)
    curr = head
    while index_to_find > 0:
        index_to_find -= 1
        curr = curr.next
    return curr.value
# Time Complexity : O(N)
# Space Complexity : O(1)

def find_middle_of_linkedlist_second_approach(head):
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow.value
    
# Time Complexity : O(N)
# Space Complexity : O(1)

def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    # print(find_middle_of_linkedlist_first_approach(head))
    print(find_middle_of_linkedlist_second_approach(head))
    head.next.next.next.next.next = ListNode(6)
    # print(find_middle_of_linkedlist_first_approach(head))
    print(find_middle_of_linkedlist_second_approach(head))
    head.next.next.next.next.next.next = ListNode(7)

main()