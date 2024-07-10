class BinarySearchTree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self,data):
            self.data = data
            self.left = self.right = None

    def insert(self,data):
        if root is None:
            return self.Node(data)
        elif root.data > data:
            root.left = self.insert(root.left,data)
        elif root.data < data:
            root.right = self.insert(root.right,data)
        else:
            return root

    def preorder(self,root):
        if root is None:
            return
        self.preorder(root.left)
        print(root.data, end=' ')
        self.preorder(root.right)




if __name__ == "__main__":
    root = BinarySearchTree()




