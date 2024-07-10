def binarySearch(list,data):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if list[mid] == data:
            return mid
        elif list[mid] < data:
            high = mid - 1
        elif list[mid] > data:
            low = mid + 1
    return -1


def linearSearch(list,data):
    for i in range(len(list)):
        if list[i] == data:
            return True
    return False


if __name__ == "__main__":
    pass
