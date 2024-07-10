def gridTraveler(m,n):
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1

    return gridTraveler(m-1,n) + gridTraveler(m,n-1)

def gridTraveler1(m,n,memo={}):
    if m == 0 or n == 0:
        return 0
    if m == 1 or n == 1:
        return 1
    key = str(m) + '-' + str(n)
    if key in memo:
        return memo[key]
    memo[key] = gridTraveler1(m-1,n,memo) + gridTraveler1(m,n-1,memo)
    return memo[key]

if __name__ == "__main__":
    print(gridTraveler1(20,12))
    print(gridTraveler(20,12))