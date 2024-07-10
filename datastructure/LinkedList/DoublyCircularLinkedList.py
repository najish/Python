class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self,data):
            self.data = data
            self.prev = self.next = None

    """
        Different Kind of Operations
        1. Insertion
            * At the Beginning
            * At the end
            * After a given Node
            * Before a given Node
        2. Deletion
            * From the beginning
            * from the end
            * a specific node
        3. Traversal
            * Forward Traversal
            * Backward Traversal
        4. Searching
            * Search for an element
        5. Updating
            * Update a node's value
        6. Display
            * display forward
            * display backward
        7. Other Operations
            * count the nodes
            * check for emptiness
            * concatenate two list
    
    """


    """
        1. Insertion Operation
            * at first
            * at last
            * after a given node
            * before a given node
    """
    def insertAtFirst(self,data):
        current = self.head
        if current is None:
            node = self.Node(data)
            node.prev = node
            node.next = node
            self.head = node
        else:
            node = self.Node(data)
            last = current.prev
            last.next = node
            current.prev = node
            node.next = current
            node.prev = last
            self.head = node

    def insertAtLast(self,data):
        current = self.head
        if current is None:
            node = self.Node(data)
            node.prev = node
            node.next = node
            self.head = node
        else:
            """
                I have to change 4 four references
                last node ->next
                head node ->prev
                two changes of the new node
            """
            node = self.Node(data)
            last = current.prev
            current.prev = node
            last.next = node
            node.next = current
            node.prev = last




    """
        Deletion 
    """
    def removeFirst(self):
        current = self.head
        if current is None:
            print("List is already emptyyy")
        else:
            next = current.next
            if next is current:
                self.head = None
            else:
                last = current.prev
                next = current.next
                if last is next:
                    next.next = next
                    next.prev = next
                    self.head = next
                else:
                    last.next = next
                    next.prev = last
                    self.head = next




    def removeLast(self):
        current = self.head
        if current is None:
            print("List is already empty")
        else:
            last = current.prev
            if last is current:
                self.head = None
            else:
                prev = last.prev
                prev.next = current
                current.prev = prev
                self.head = current

    def removeNode(self,data):
        current = self.head
        if current is None:
            print("list is empty")
        else:
            if (current.data == data) and (current.next is current) and (current.prev is current):
                self.head = None
            else:
                while current.next != self.head:
                    if current.data == data:
                        pass
                    current = current.next



    def printList(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            while current.next != self.head:
                print(current.data, end='->')
                current = current.next
            print(current.data)


    def countNodes(self):
        current = self.head
        if current is None:
            return 0
        else:
            count = 0
            while current.next != self.head:
                count += 1
                current = current.next
            return count + 1


if __name__ == "__main__":
    dlist = DoublyCircularLinkedList()
    dlist.insertAtFirst(10)
    dlist.insertAtFirst(20)
    dlist.insertAtFirst(30)
    dlist.insertAtFirst(40)
    dlist.insertAtLast(500)
    dlist.insertAtLast(500)
    dlist.printList()
    dlist.removeFirst()
    dlist.removeFirst()
    dlist.removeFirst()
    dlist.removeLast()
    dlist.removeFirst()
    dlist.removeFirst()
    dlist.printList()















