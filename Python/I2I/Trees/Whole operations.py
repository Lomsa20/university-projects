class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def preorderTraversal(node):
    if node is None:
        return
    print(node.data, end = ", ")
    preorderTraversal(node.left)
    preorderTraversal(node.right)
def inorderedTraversal(node):
    if node is None:
        return
    inorderedTraversal(node.left)
    print(node.data, end = ", ")
    inorderedTraversal(node.right)

def postorderedeTraversal(node):
    if node is None:
        return
    postorderedeTraversal(node.left)
    postorderedeTraversal(node.right)
    print(node.data, end = ", ")

def BST(node,target):
    if node is None:
        return
    elif node.data == target:
        return target
    elif node.data > target:
        return BST(node.left, target)
    else:
        return BST(node.right, target)
def insert(node, Ndata):
    if node is None:
        return TreeNode(Ndata)
    else:
        if node < Ndata:
            node.right = insert(node.right, Ndata)
        elif node >Ndata:
            node.left = insert(node.left, Ndata)
        return node

def lowest(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(node,data):
    if not node:
        return None
    if node > data:
        node.left = delete(node.left, data)
    elif node < data:
        node.right = delete(node.right, data)
    else:
        # Node with only one Child or No child
        if not node.left:#checks if node has any left child
            temp = node.right
            node = None
            return temp
        elif not node.right:
            temp = node.left #replace left node
            node = None #deletion happend here
            return temp
    #Node with two children get the in-order successor
        node.data=lowest(node.right).data
        node.right=delete(node.right, node.data)
    return node



root = TreeNode("R")
nodeA = TreeNode("A")
nodeB = TreeNode("B")
nodeC = TreeNode("C")
nodeD = TreeNode("D")
nodeE = TreeNode("E")
nodeF = TreeNode("F")
nodeG = TreeNode("G")

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG
print("TreeNode:")
preorderTraversal(root.right.left)

