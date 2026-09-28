class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    def build_tree(preorder,inorder):
        if not preorder or not inorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        idx = inorder.index(root_val)
        root.left = build_tree(preorder[1:idx + 1], inorder[:idx])
        root.right = build_tree(preorder[idx +1:], inorder[idx+1:])
        return root