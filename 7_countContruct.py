## Description ##
# Returns the number of ways that the 'target' can be constructed by concatenating elements of the 
# 'wordBank' array.
# Returns false if 'target' can't be constructed.
# 
# Reuse of elements in wordBank is allowed.

## Complexity ##
# let n = len(wordBank) and m = len(target)
#
# Before memoization:
# Time complexity is O(n^m * m) because the strip function needs to iterate through the string.
# Space complexity is O(m^2) because the second m is required to store the suffix at worst case. 
# 
# After memoization:
# Time complexity is O(n*m^2).
# Space complexity is O(m^2).

## Note ##
# Python doesn't seem to run into exponential time complexity for the last test case without 
# memoization if lstrip is used. If the string slicing method is used instead then we get the 
# expected slowdown.

def countConstruct(target, wordBank, memo = None):
    if memo is None: memo = {}
    
    if target in memo: return memo[target]
    if target == '': return 1
    
    result = 0 
    for word in wordBank:
        if target.startswith(word):
            # suffix = target.lstrip(word)
            suffix = target[len(word):]
            result += countConstruct(suffix, wordBank, memo)

    memo[target] = result
    return result

print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(countConstruct('enterapotentpot', ['a','p','ent','enter','ot','o','t']))
print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e','ee','eee','eeee','eeeee','eeeeee']))