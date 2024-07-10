class queueArray:
    def __init__(self):
        self.arr = None
        self.rear = -1
        self.front = -1


    def enqueue(self,data):
        arr = self.arr
        if arr is None:
            self.arr = []

        self.arr.insert(0,data)
        self.rear = 0