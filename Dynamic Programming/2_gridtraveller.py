# Given a grid of n rows by m columns, how many ways can a person move from the 
# top left to the bottom right if he can only move down or to the right?

# If solved recursively, O(2^(n+m)) time and O(n+m) space. n+m space because we 
# need to reduce n and m by 1 alternatively until they become 1 or 0. Remove 
# lines 15-20 and 25 to get the recursive solution.

# Using dynamic programming, O(n*m) in time and O(n+m) space. n*m time because 
# you only need to go through n*m permutations of nodes and do not need to \
# repeat the same cases.

def gridtraveller(n, m, memo = {}):
    # since (n,m) and (m,n) cases are interchangeable, we can optimise the key 
    # storage further.
    if n <= m : 
        key = str(n) + ',' + str(m)
    else:
        key = str(m) + ',' + str(n)

    if key in memo: return memo[key]
    
    if n == 0 or m == 0: return 0
    if n == 1 or m == 1: return 1

    memo[key] = gridtraveller(n-1,m,memo) + gridtraveller(n,m-1,memo)
    return memo[key]

print(gridtraveller(18,18))

