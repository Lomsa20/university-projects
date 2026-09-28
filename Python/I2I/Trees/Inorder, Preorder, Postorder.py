class Node:
    def __init__(self,data):
        self.data = data
        self.left , self.right = None, None
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.data > key:
            root.left = insert(root.left,key)
        elif root.data < key:
            root.right = insert(root.right,key)
        # if key == root.data: do nothing
    return root
def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.data)
    inorder(root.right)
def preorder(root):
    if root is None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)
root = Node(78)
insert(root,8)
insert(root,9)
insert(root,123)
inorder(root)
preorder(root)
postorder(root)
