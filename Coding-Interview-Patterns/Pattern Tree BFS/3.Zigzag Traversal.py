# Problem Statement #
# Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the values of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels.

from collections import deque

class TreeNode:
    def __init__(self,value=0,left=None,right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

def zigzag_traversal(root):
    result = []
    queue = deque()
    queue.append(root)
    leftToRight = True
    while queue:
        queue_size = len(queue)
        curr_level = deque()
        for _ in range(queue_size):
            node = queue.popleft()
            if leftToRight:
                curr_level.append(node.value)
            else:
                curr_level.appendleft(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(list(curr_level))
        leftToRight = not leftToRight
    return result
            
            



def main():
    root = TreeNode(100)
    root.left = TreeNode(90)
    root.right = TreeNode(110)
    root.left.left = TreeNode(80)
    root.left.right = TreeNode(85)
    root.right.left = TreeNode(105)
    root.right.right = TreeNode(120)
    print(zigzag_traversal(root))
main()

# Time Complexity: O(N)
# Space Complexity: O(N)