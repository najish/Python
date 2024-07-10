def canSum(numbers,target, memo= {}):
    if target in memo:
        return memo[target]
    if target < 0:
        return False
    if target == 0:
        return True
    for number in numbers:
        memo[target] = canSum(numbers,target - number,memo)
        if memo[target] == True:
            return True
    memo[target] = False
    return False
def how_sum(target_sum, numbers, memo=None):
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in numbers:
        remainder = target_sum - num
        remainder_result = how_sum(remainder, numbers, memo)
        if remainder_result is not None:
            memo[target_sum] = remainder_result + [num]
            return memo[target_sum]

    memo[target_sum] = None
    return None


def howSum(target, numbers, memo = None):
    if memo is None:
        memo = {}
    if target < 0:
        return None
    if target == 0:
        return []
    if target in memo:
        return memo[target]
    for number in numbers:
        rem = target - number
        result = howSum(rem, numbers, memo)
        if result is not None:
            memo[target] = result + [number]
            return memo[target]

    memo[target] = None
    return None