class LinkedList:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    # insertion operation are of 3 types in singly linkedlist
    # 1. InsertAtFirst 2. InsertAtLast 3.InsertAtIndex/InsertAtPosition
    def insertAtFirst(self,data):
        current = self.Node(data)
        current.next = self.head
        self.head = current



    def insertAtLast(self,data):
        head = self.head
        if head is None:
            head = self.Node(data)
        else:
            current = head
            while current.next != None:
                current = current.next
            current.next = self.Node(data)


    def insertAtIndex(self,index,data):
        current = self.head
        count = 0
        prev = None
        while current != None:
            count += 1
            if count == index:
                if prev is None:
                    temp = self.Node(data)

            prev = current
            current = current.next
        print("invalid given index position")

    # Traversal Operation
    def printList(self):
        current = self.head
        while current != None:
            print(current.data, end= '->')
            current = current.next
        print()


    # Searching Operation

    def isContains(self,data):
        current = self.head
        while current != None:
            if current.data == data:
                return True
            current = current.next
        return False

    # Find the Index of the node of the given value

    def findIndex(self,data):
        current = self.head
        index = -1
        if current == None:
            return -1

        while current != None:
            index += 1
            if current.data == data:
                return index
            current = current.next
        return -1


    # find the index from the last
    def findLastIndex(self,data):
        current = self.head
        index = -1
        lastIndex = None
        while current != None:
            index += 1
            if current.data == data:
                lastIndex = index
            current = current.next
        if lastIndex == None:
            return -1
        else:
            return lastIndex

if __name__ == "__main__":
    list1 = LinkedList()

    list1.insertAtFirst(10)
    list1.insertAtFirst(20)
    list1.insertAtFirst(30)
    list1.insertAtFirst(40)
    list1.insertAtFirst(50)
    list1.insertAtLast(10)
    list1.insertAtLast(20)
    list1.insertAtLast(30)
    list1.insertAtLast(40)
    list1.insertAtLast(50)
    list1.printList()
    print(list1.findLastIndex(50))