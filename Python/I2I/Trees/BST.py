class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def BST(node, target):
    if node is None:
        return None
    if node.data == target:
        return node
    if target < node.data:
        return BST(node.left, target)
    else:
        return BST(node.right, target)
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.right = TreeNode(20)
res = BST(root, 15)
if res:
    print(res.data)
else:
    print(-1)
