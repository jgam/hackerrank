def inOrder(root):
    #Write your code here
    #inOrder traversal starts from the leftmost node and hits its root
    #then, moves to the right child.
    
    #check if there is left child
    if root.left:
        inOrder(root.left)
    #if not, print the current node's value
    print(root.info, end =" ")
    
    #check if right child exists
    if root.right:
        inOrder(root.right)
    