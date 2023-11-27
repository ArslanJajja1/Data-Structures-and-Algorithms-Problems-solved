# Problem Statement #
# Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., the lowest level comes first. You should populate the values of all nodes in each level from left to right in separate sub-arrays.

from collections import deque

class TreeNode:
    def __init__(self,value=0,left=None,right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

def reverse_bfs(root):
    result = deque()
    queue = deque()
    queue.append(root)
    while queue:
        curr_level = []
        queue_size = len(queue)
        for _ in range(queue_size):
            node = queue.popleft()
            curr_level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.appendleft(curr_level)
    return result
        
    


def main():
    root = TreeNode(100)
    root.left = TreeNode(90)
    root.right = TreeNode(110)
    root.left.left = TreeNode(80)
    root.left.right = TreeNode(85)
    root.right.left = TreeNode(105)
    root.right.right = TreeNode(120)
    print(reverse_bfs(root))
main()