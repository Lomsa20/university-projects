def is_balanced(root):
    def check(node):
        if not node:
            return 0, True
        lh,lb = check(node.left)
        rh,rb = check(node.right)
        balanced = lb and rb and abs(lh - rh) <= 1
        return max(lh,rh) + 1, balanced
    return check(root)