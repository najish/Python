class stackLinkedList:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None



    def push(self,data):
        current = self.head
        node = self.Node(data)
        node.next = current
        self.head = node

    def pop(self):
        current = self.head
        if current is None:
            print("stack is already empty")
            return
        else:
            data = current.data
            self.head = current.next
            return data
    def peek(self):
        current = self.head
        if current is None:
            return None
        else:
            return current.data



if __name__ == "__main__":
    stack = stackLinkedList()
    stack.push(10)
    stack.push(29)
    stack.push(30)
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.peek())