class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
    

# Check for cycle in linked list
def check_cycle(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print("Has cycle ", str(check_cycle(head)))
    head.next.next.next.next.next = head.next.next
    print("Has cycle ", str(check_cycle(head)))
main()
