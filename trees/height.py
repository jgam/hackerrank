def height(root):
    add = 0
    if root.left:
        add = 1 + height(root.left)
    if root.right:
        add = 1 + height(root.right)
    return add
    