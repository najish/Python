class stackArray:
    def __init__(self):
        self.arr = None
        self.top = -1

    def push(self,data):
        arr = self.arr
        if arr is None:
            self.arr = []
        self.arr.append(data)
        self.top += 1

    def pop(self):
        arr = self.arr
        if arr is None:
            return
        else:
            arr.pop()
            if len(self.arr) == 0:
                self.top = -1
                self.arr = None
            elif len(self.arr) >= 1:
                self.top -= 1

    def peek(self):
        arr = self.arr
        if arr is None:
            return arr
        else:
            return self.arr[self.top]

    def isEmpty(self):
        arr = self.arr
        if arr is None:
            return True
        return False


if __name__ == "__main__":
    s = stackArray()
    s.push(10)
    s.push(20)
    s.pop()
    s.pop()
    s.push(50)
    print(s.peek())