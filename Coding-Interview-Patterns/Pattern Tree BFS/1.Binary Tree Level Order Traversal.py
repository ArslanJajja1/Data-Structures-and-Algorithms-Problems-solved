# Problem Statement #
# Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.

from collections import deque
class TreeNode:
    def __init__(self,value=0,left=None,right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

def traverse(root):
    result = []
    if root is None:
        return root
    queue = deque()
    queue.append(root)
    while queue:
        queue_size = len(queue)
        curr_level = []
        for _ in range(queue_size):
            node = queue.popleft()
            curr_level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(curr_level)
    return result
    



def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print("Level order traversal: " + str(traverse(root)))
main()

# Time Complexity : O(N)
# Space Complexity : O(N)