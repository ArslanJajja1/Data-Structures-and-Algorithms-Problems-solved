# 145. Binary Tree Postorder Traversal
# Easy
# 5.9K
# 173
# Companies
# Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [3,2,1]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
 

# Constraints:

# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive 

        # result = []
        # def helper(root):
        #     if not root:
        #         return
        #     helper(root.left)
        #     helper(root.right)
        #     result.append(root.val)
        # helper(root)
        # return result

        # TC : O(N)
        # SC : O(N)

        # Iterative 
        stack = [root]
        visit = [False]
        res = []
        while stack:
            curr,v = stack.pop(),visit.pop()
            if curr:
                if v:
                    res.append(curr.val)
                else:
                    stack.append(curr)
                    visit.append(True)
                    stack.append(curr.right)
                    visit.append(False)
                    stack.append(curr.left)
                    visit.append(False)
        return res

        # TC : O(N)
        # SC : O(N)
