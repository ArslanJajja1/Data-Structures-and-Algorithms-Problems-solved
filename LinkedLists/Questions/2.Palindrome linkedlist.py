# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

       #* First approach - using additional data structure

        #* arr = []
        #* temp = head
        #* while temp:
        #*    arr.append(temp.val)
        #*    temp = temp.next
        #* n = len(arr)
        #* for i in range(n):
        #*     if arr[i] != arr[n-i-1]:
        #*         return False
        #* return True

        #* TC : O(N)
        #* SC : O(N)

        #* Second approach - without using additional data structure

        #* Step 1 : Find the middle of linkedlist
        #* Step 2 : Reverse the linked list from middle to end
        #* Step 3 : Iterate from start to middle and compare node values
        #* like compare start val   with the mid next node value and so on.
        #* Step 4 : if they are not equal return False
        if not head or not head.next:
            return head
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = self.reverse_list(slow.next)
        temp = slow.next
        dummy = head
        while temp:
            if dummy.val != temp.val:
                break
            dummy = dummy.next
            temp = temp.next
        slow.next = self.reverse_list(slow.next)
        if temp != None:
            return False
        return True
    #* Reverse a linked list
    def reverse_list(self,head):
        prev = None
        while head:
            head_next = head.next
            head.next = prev
            prev = head
            head = head_next
        return prev
    
    #* TC : O(N)
    #* SC : O(1)
        





