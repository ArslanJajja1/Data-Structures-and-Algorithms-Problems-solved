# Kth largest element in Binary search tree
class Solution:
    def kthLargest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.right
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.left
# SC : O(h+k)
# SC : O(h)