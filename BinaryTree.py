import time
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        if self.data:
            if self.data > data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            if self.data < data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    def traverse(self, root):
        result = []
        if root:
            result = self.traverse(root.left)
            result.append(root.data)
            result = result + self.traverse(root.right)
        return result

    def preorder(self, root):
        result = []
        if root:
            result.append(root.data)
            result += self.preorder(root.left)
            result += self.preorder(root.right)
        return result

    def postorder(self, root):
        result = [] 
        if root:
            result = self.postorder(root.left)
            result += self.postorder(root.right)
            result.append(root.data)
        return result

root = Node(5)
root.insert(10)
root.insert(2)
root.insert(1)
root.insert(4)
root.insert(11)
root.insert(12)



print(root.postorder(root))
