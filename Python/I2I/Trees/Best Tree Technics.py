class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.data:
            root.left = self._insert(root.left, key)
        elif key > root.data:
            root.right = self._insert(root.right, key)
        # if equal → ignore duplicate

        return root
    def treesum(self, root):
        if root is None:
            return 0
        else:
            leftsum = self.treesum(root.left)
            rightsum = self.treesum(root.right)
            return root.data + leftsum + rightsum
    def treeMax(self, root):
        if root is None:
            return float('-inf')
        else:
            leftMax = self.treeMax(root.left)
            rightMax = self.treeMax(root.right)
            return max(root.data, leftMax,rightMax)
    def treeHeight(self, root):
        if root is None:
            return 0, True
        else:
            leftHeight, rightHeight = self.treeHeight(root.left), self.treeHeight(root.right)
            return max(leftHeight, rightHeight) + 1
    def existsInTree(self, root, value):
        if root is None:
            return False
        else:
            inLeft = self.existsInTree(root.left, value)
            inRight = self.existsInTree(root.right, value)
            return root.data == value or inLeft or inRight
    def reverseTree(self, root):
        if root is None:
            return
        else:
            self.reverseTree(root.left)
            self.reverseTree(root.right)
            root.left, root.right = root.right, root.left