def insertion(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1
        while j >= 0 and list[j] > temp:
            list[j+1] = list[j]
            j -= 1
        list[j + 1] = temp


def insertionReverse(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and list[j] < key:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key


def insertionSort(list,ascending = True):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        if ascending == True:
            while j >= 0 and list[j] > key:
                list[j+1] = list[j]
                j -= 1
            list[j+1] = key
        else:
            while j >= 0 and list[j] < key:
                list[j+1] = list[j]
                j -= 1
            list[j+1] = key



def insertionEarlyTermination(list):
    pass



def bubble(list):
    pass

def selection(list):
    pass

def merget(list):
    pass

def quick(list):
    pass


if __name__ == "__main__":
    list = [1,2,7,4]
    insertionSort(list,False)
    print(list)
