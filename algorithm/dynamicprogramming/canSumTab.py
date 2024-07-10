def canSumTab(target,list):
    result = [False] * (target + 1)
    result[0] = True
    for i in range(len(result)):
        if result[i] == True:
            for x in list:
                if i + x < len(result):
                    result[i + x] = True

    print(result)
    return result[target]







if __name__ == "__main__":
    target = 7
    list = [3,4,2]
    canSumTab(target,list)