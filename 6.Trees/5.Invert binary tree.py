# 226. Invert Binary Tree
# Easy
# 12.1K
# 172
# Companies
# Given the root of a binary tree, invert the tree, and return its root.

 

# Example 1:


# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:


# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursive

        if not root:
            return None
        temp = root.right
        root.right = root.left
        root.left = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        
        # Iterative
        def swap(node):
            if not node:
                return
            temp = node.right
            node.right = node.left
            node.left = temp

        if not root:
            return None
        q = collections.deque()
        q.append(root)
        
        while q:
            curr = q.popleft()
            swap(curr)
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
        return root
        

        # TC : O(N)
        # SC : O(N)
            
