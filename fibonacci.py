# fibonacci recursion
def fib_rec(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)
print(fib_rec(10))


#fibonacci memo
memo = {
    1: 1,
    2: 1
}
def fib_mem(n):
    if n in memo:
        return memo[n]
    else:
        res = fib_mem(n - 1) + fib_mem(n - 2)
        memo[n] = res
        return res
print(fib_mem(10))


#fibonacci memo 2
def fib_mem2(n):
    if n in memo:
        return memo[n]
    res = fib_mem2(n - 1) + fib_mem2(n - 2)
    memo[n] = res
    return res
print(fib_mem2(10))