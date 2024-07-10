def insertion(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1

        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key


def insertion_reverse(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1

        while j >= 0 and list[j] < key:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key



def count_shits(list):
    total = 0

    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        count = 0
        while j >= 0 and list[j] > key:
            list[j+1] = list[j]
            j -= 1
            count += 1
        list[j+1] = key
        total += count
    return total


def check(str1, str2):
    if str1 == "":
        return True
    elif str2 == "":
        return False

    for i in range(str)

def insertion_string(list):
    for i in range(1,len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and check(key,list[j]) == False:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key


if __name__ == "__main__":
    list = [1,2,7,4,5]
    list2 = [5,4,3,2,1]
    print(count_shits(list))
    print(count_shits(list2))