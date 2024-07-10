class BinarySearchTree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self,data):
            self.data = data
            self.left = self.right = None

    def insert(self,data):
        root = self.root
        if root is None:
            self.root = self.Node(data)

        parent = None
        while root is not None:
            if root is None:
                root = self.Node(data)
                

