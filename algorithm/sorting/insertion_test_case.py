from pathlib import Path
def insertion(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1
        while j >= 0 and list[j] > temp:
            list[j+1] = list[j]
            j -= 1
        list[j + 1] = temp



def create_test_case():
    file = open("E:\\Learn\\python\\algorithm\\sorting","w")
    for i in range(1,11):
        file.write(i)



if __name__ == "__main__":

    create_test_case()


    # file = open('E:\\Learn\\python\\algorithm\\sorting\insertion.txt')
    #
    # x = file.readline().split(' ')
    # list = []
    # for y in x:
    #     list.append(int(y))
    #
    # print(list)
    #
    # file.close()
    #
    # insertion(list)
    # print(list)

    create_test_case()