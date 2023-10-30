# Problem Statement #
# Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.

class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

def has_cycle_first_solution(head):
    hashmap = {}
    while head:
        if head in hashmap:
            return True
        hashmap[head] = True
        head = head.next
    return False
# Time Complexity : O(N)
# Space Complexity : O(N)

def has_cycle_second_solution(head):
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False
# Time Complexity : O(N)
# Space Complexity : O(1)

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    if(has_cycle_second_solution(head)):
        print('LinkedList has cycle.')
    else:
        print('LinkedList does not has cycle.')
    head.next.next.next.next.next.next = head.next.next.next
    if(has_cycle_second_solution(head)):
        print('LinkedList has cycle.')
    else:
        print('LinkedList does not has cycle.')
main()


