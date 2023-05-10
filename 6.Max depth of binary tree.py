# 104. Maximum Depth of Binary Tree
# Easy
# 10.7K
# 171
# Companies
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive

        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left,right)

        # TC : O(N)
        # SC : O(N)

        # Iterative
        if not root:
            return 0
        q = collections.deque()
        q.append(root)
        depth = 0
        while q:
            depth += 1
            for i in range(len(q)):
                temp = q.popleft()
                if temp.left is not None: q.append(temp.left)
                if temp.right is not None: q.append(temp.right)
        return depth

        # TC : O(N)
        # SC : O(N)




