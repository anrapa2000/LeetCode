class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:   
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
    
    def inOrderTraversal(self, root):
        res = []

        def inorder(root):
            if not root:
                return
            else:
                inorder(root.left)
                res.append(root.data)
                inorder(root.right)
        inorder(root)
        return res
    
    def preOrderTraversal(self, root):
        res = []

        def preOrder(root):
            if not root:
                return
            else:
                res.append(root.data)
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)
        return res
    
    def postOrderTraversal(self, root):
        res = []

        def postOrder(root):
            if not root:
                return
            else:
                postOrder(root.left)
                postOrder(root.right)
                res.append(root.data)
        postOrder(root)
        return res

            
    
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inOrderTraversal(root))  
print(root.preOrderTraversal(root))
print(root.postOrderTraversal(root))