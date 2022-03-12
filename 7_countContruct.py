## Description ##
# Returns the number of ways that the 'target' can be constructed by concatenating elements of the 
# 'wordBank' array.
# Returns 0 if 'target' can't be constructed.
# 
# Reuse of elements in wordBank is allowed.

## Complexity ##
# let n = len(wordBank) and m = len(target)
#
# Before memoization:
# Time complexity is O(n^m * m) because the suffix line needs to iterate through the string.
# Space complexity is O(m^2) because the second m is required to store the suffix at worst case. 
# 
# After memoization:
# Time complexity is O(n*m^2).
# Space complexity is O(m^2).

def countConstruct(target, wordBank, memo = None):
    if memo is None: memo = {}
    
    if target in memo: return memo[target]
    if target == '': return 1
    
    numOfWays = 0 
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            numOfWays += countConstruct(suffix, wordBank, memo)

    memo[target] = numOfWays
    return numOfWays

print(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(countConstruct('enterapotentpot', ['a','p','ent','enter','ot','o','t']))
print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e','ee','eee','eeee','eeeee','eeeeee']))