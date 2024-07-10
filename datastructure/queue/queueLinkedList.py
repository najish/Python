class queueLinkedList:
    def __init__(self):
        self.rear = None
        self.front = None
        self.size = 0


    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None



    def enqueue(self,data):
        current = self.rear
        if current is None:
            node = self.Node(data)
            self.rear = self.front = node
        else:
            node = self.Node(data)
            node.next = current
            self.rear = node
        self.size += 1

    def dequeue(self):
        front = self.front
        rear = self.rear

        if rear is front:
            self.rear = self.front = None
        else:
            while rear.next is not front:
                rear = rear.next
            rear.next = None
            self.front = rear
        if self.size >= 1:
            self.size -= 1

    def frontValue(self):
        front = self.front
        if front is None:
            return
        else:
            return front.data

    def rearValue(self):
        rear = self.rear
        if rear is None:
            return
        else:
            return rear.data

    def isEmpty(self):
        rear = self.rear
        front = self.front
        if rear is front and rear is None:
            return True
        else:
            return False


    def clear(self):
        self.rear = self.front = None
        self.size = 0



if __name__ == "__main__":
    queue = queueLinkedList()
    queue.enqueue(10)
    queue.enqueue(20)
    print(queue.rearValue())
    print(queue.frontValue())
    queue.dequeue()
    print(queue.rearValue())
    print(queue.frontValue())
    queue.dequeue()
    queue.dequeue()
    print(queue.frontValue())
    print(queue.rearValue())
    print(queue.isEmpty())
    queue.enqueue(50)
    print(queue.isEmpty())