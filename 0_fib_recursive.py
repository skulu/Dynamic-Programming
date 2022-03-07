# Classic recursive implementation for fibonacci sequence
# Slow, O(2^n) in time O(n) in space

def fib(n):
    if n <= 2: return 1
    return (fib(n-2) + fib(n-1))

print(fib(50))
