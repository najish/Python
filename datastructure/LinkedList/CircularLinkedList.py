class CircularLinkedList:
    def __init__(self):
        self.head = None


    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None



    # Operations on singly circular linked list
    # insertion, deletion, traversal, search

    def insertAtLast(self,data):
        current = self.head
        if current == None:
            node = self.Node(data)
            node.next = node
            self.head = node
        else:
            while current.next != self.head:
                current = current.next
            node = self.Node(data)
            node.next = self.head
            current.next = node

    def printList(self):
        current = self.head
        if current == None:
            print("List is empty")
        else:
            while current.next != self.head:
                print(current.data, end='->')
                current = current.next
            print(current.data)
            print()

    def insertAtFirst(self,data):
        current = self.head
        node = self.Node(data)
        if current == None:
            node.next = node
            self.head = node
        else:
            while current.next != self.head:
                current = current.next
            node.next = self.head
            current.next = node
            self.head = node

    def isContains(self,data):
        current = self.head
        if current == None:
            return False
        else:
            while current.next != self.head:
                if current.data == data:
                    return True
                current = current.next
            if current.data == data:
                return True
        return False

if __name__ == "__main__":
    list = CircularLinkedList()

    list.insertAtFirst(10)
    list.insertAtFirst(10)
    list.insertAtFirst(10)
    list.printList()
