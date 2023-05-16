# 144. Binary Tree Preorder Traversal
# Easy
# 6.8K
# 175
# Companies
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# Follow up: Recursive solution is trivial, could you do it iteratively?

# Accepted
# 1.3M
# Submissions
# 2M
# Acceptance Rate
# 67.1%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive

        # result = []
        # def helper(root):
        #     if not root:
        #         return 
        #     result.append(root.val)
        #     helper(root.left)
        #     helper(root.right)
        # helper(root)
        # return result
        
        # TC : O(N)
        # SC : O(N)

        # Iterative
        res,stack = [],[]
        curr = root
        while curr or stack:
            while curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            curr = stack.pop()
        return res

        # TC : O(N)
        # SC : O(N)





