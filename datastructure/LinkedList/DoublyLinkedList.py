class DoublyLinkedList:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self,data):
            self.data = data
            self.prev = self.next = None

    def printList(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            while current.next is not None:
                print(current.data, end='->')
                current = current.next
            print(current.data)


    def insertAtFirst(self,data):
        current = self.head
        if current is None:
            node = self.Node(data)
            self.head = node
        else:
            node = self.Node(data)
            node.next = self.head
            self.head = node


    def insertAtLast(self,data):
        current = self.head
        if current is None:
            node = self.Node(data)
            self.head = node
        else:
            while current.next is not None:
                current = current.next
            current.next = self.Node(data)


    def insertAtIndex(self,index,data):
        i = -1
        current = self.head
        prev = None
        while current.next is not None:
            i += 1
            if i == index:
                current

    def printList(self):
        current = self.head
        if current is None:
            print("List is empty")
            return


        while current is not None:
            print(current.data, end='->')
            current = current.next
        print()


    def findIndex(self,data):
        current = self.head
        index = -1
        while current is not None:
            index += 1
            if current.data == data:
                return index
        return -1

    def findLastIndex(self,data):
        index = -1
        i = -1
        current = self.head
        while current is None:
            i += 1
            if current.data == data:
                index = i
            current = current.next
        return index

    def isContains(self,data):
        current = self.head
        while current is None:
            if current.data == data:
                return True
            current = current.next
        return False


if __name__ == "__main__":
    list = DoublyLinkedList()
    list.insertAtLast(10)
    list.insertAtLast(10)
    list.insertAtLast(10)
    list.insertAtLast(10)
    list.insertAtLast(10)
    list.insertAtFirst(20)
    list.insertAtFirst(20)
    list.insertAtFirst(20)
    list.printList()