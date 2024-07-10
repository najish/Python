class stackArray:
    def __init__(self):
        self.arr = None
        self.top = -1


    def push(self,data):
        arr = self.arr
        if arr is None:
            self.arr = []
            self.arr.append(data)
            self.top = 0
        else:
            self.arr.append(data)
            self.top += 1

    def pop(self):
        arr = self.arr
        if arr is None:
            return
        elif len(arr) >= 1:
            arr.pop()
            self.top -= 1
        else:
            self.arr = None
            self.top = -1


    def peek(self):
        arr = self.arr
        if arr is None:
            return
        else:
            return arr[self.top]



if __name__ == "__main__":
    s = stackArray()
    s.push(10)
    print(s.peek())