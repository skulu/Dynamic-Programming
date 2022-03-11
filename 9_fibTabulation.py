# O(n) in time and space. Possible to optimise further in space by only keeping last 2 elements of 
# fib sequence everytime.

def fib(n):
    result = [0 for i in range(n+1)]
    result[1] = 1

    if n < 2: return result[n]

    for i in range(2,n+1):
        result[i] = result[i-2] + result[i-1]

    return result[n]

print(fib(10))