import re


class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTheTree(self):
        if self.left:
            self.left.printTheTree()
        print(self.data)
        if self.right:
            self.right.printTheTree()
# * Inorder traversal
# * Left -> Root -> Right

    def inorder(self, root):
        result = []
        if root:
            result = self.inorder(root.left)
            result.append(root.data)
            result = result + self.inorder(root.right)
        return result

    def preorder(self, root):
        result = []
        if root:
            result.append(root.data)
            result = result+self.preorder(root.left)
            result = result+self.preorder(root.right)
        return result

    def postorder(self, root):
        result = []
        if root:
            result = self.postorder(root.left)
            result = result+self.postorder(root.right)
            result.append(root.data)
        return result


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.printTheTree()
print(root.inorder(root))
print(root.preorder(root))
print(root.postorder(root))
