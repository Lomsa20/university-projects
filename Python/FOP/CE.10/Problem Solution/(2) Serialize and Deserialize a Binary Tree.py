class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def serialize(root):
    vals = []
    def dfs(node):
        if not node:
            vals.append("#")
            return
        vals.append(str(node.val))
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return " ".join(vals)
def deserialize(s):
    vals = iter(data.split())
    def dfs():
        val = next(vals)
        if val == "#":
            return None
        node = TreeNode(int(val))
        node.left = dfs()
        return node
    return dfs()
