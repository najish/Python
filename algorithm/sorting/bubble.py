def bubble(list):
    for i in range(len(list)):
        for j in range(1, len(list)):
            if list[j - 1] > list[j]:
                temp = list[j - 1]
                list[j - 1] = list[j]
                list[j] = temp




def bubbleSort(list):
    for i in range(len(list)):
        for j in range(1, len(list) - i):
            if list[j - 1] > list[j]:
                temp = list[j-1]
                list[j-1] = list[j]
                list[j] = temp



if __name__ == "__main__":
    list = [10,30,20,50,40,5]
    list2 = [50,50,40,30,20,5,10]
    bubbleSort(list)
    print(list)
    bubble(list2)
    print(list2)