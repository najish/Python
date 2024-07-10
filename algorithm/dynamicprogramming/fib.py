def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


def fib2(n,memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib2(n-1,memo) + fib2(n-2,memo)
    return memo[n]


if __name__ == "__main__":
    print(fib(1))
    print(fib(10))

    print(fib2(1))
    print(fib2(40))