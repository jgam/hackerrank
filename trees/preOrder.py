def preOrder(root):
    if root:
        print(root.info,end = " ")
        if root.left:
            preOrder(root.left)
        if root.right:
            preOrder(root.right)
    #self.left is 
    #Write your code here
