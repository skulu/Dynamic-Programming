# Store the intermediate results so that the code does not need to continuously
# recalculate all the different fibonacci sequences and can resuse results.

# It now becomes O(n) in time and space.

# General steps to 'memo-ize':
# 1. Check if case is already in the memo
# 2. Check base cases
# 3. Store new case in memo

def fib(n, memo = {}):
    if n <= 2: return 1
    if n in memo: return memo[n]
    memo[n] = fib(n-2, memo) + fib(n-1, memo)
    return memo[n]

print(fib(50))
