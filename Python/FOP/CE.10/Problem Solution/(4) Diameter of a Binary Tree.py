def diameter(root):  # ← OUTER function
    diameter = 0     # ← OUTER variable
    def dfs(node):   # ← INNER function
        nonlocal diameter   # ← refers to the OUTER variable
        # nonlocal variable Use outer variable
        if node is None:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        diameter = max(diameter, left + right)
        return 1 + max(left, right)
    dfs(root)
    return diameter