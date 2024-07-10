def selection(list):
    for i in range(len(list) - 1):
        smallIndex = i
        small = list[i]
        for j in range(i + 1, len(list)):
            if list[i] > list[j] and small > list[j]:
                smallIndex = j
                small = list[j]
        temp = list[i]
        list[i] = list[smallIndex]
        list[smallIndex] = temp




if __name__ == "__main__":
    list = [2,1,4,3,2]
    selection(list)
    print(list)

