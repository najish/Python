def canSum(numbers, target):
    if target < 0:
        return False
    if target == 0:
        return True

    for number in numbers:
        result = canSum(numbers, target - number)
        if result == True:
            return result
    return False


def canSumOptimized(numbers,target, memo= {}):
    if target in memo:
        return memo[target]
    if target < 0:
        return False
    if target == 0:
        return True

    for number in numbers:
        memo[target] = canSumOptimized(numbers,target - number,memo)
        if memo[target] == True:
            return True
    memo[target] = False
    return False



if __name__ == "__main__":

    numbers = [4,3]
    target = 11
    print(canSumOptimized(numbers,target))