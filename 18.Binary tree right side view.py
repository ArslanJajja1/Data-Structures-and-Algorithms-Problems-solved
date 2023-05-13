# 199. Binary Tree Right Side View
# Medium
# 9.9K
# 598
# Companies
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

# Example 1:


# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]
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
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            rightNode = None
            for i in range(len(q)):
                node = q.popleft()
                if node : 
                    rightNode = node
                    q.append(rightNode.left)
                    q.append(rightNode.right)
            if rightNode:
                res.append(rightNode.val)
        return res
# TC : O(N)
# SC : O(N)