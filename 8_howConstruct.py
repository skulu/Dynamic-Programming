## Description ##
# Returns the different combinations of words that the 'target' can be constructed by concatenating 
# elements of the 'wordBank' array. Returns 2D array with each element represent 1 way of 
# construction.
# 
# Reuse of elements in wordBank is allowed.

## Base cases ##
# '' will return empty 2D array: [[]]. The empty element represents 1 way of constructing '', which 
# is to take no elements from 'wordBank'.
# 
# If the target cannot be constructed from 'wordBank', it will return []. An empty array with zero 
# ways inside, since each element of a 2D array represents a way to construct 'target', an empty 
# array has zero ways of constructing 'target'.

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

def howConstruct(target, wordBank, memo = None):
    if memo is None: memo = {}

    if target in memo: return memo[target]
    elif target == '': return [[]]
    
    result = []
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffixWays = howConstruct(suffix, wordBank, memo)
            for i in range(len(suffixWays)):
                result.append([word] + suffixWays[i])

    memo[target] = result
    return result

print(howConstruct('', ['purp', 'p', 'ur', 'le', 'purpl']))
print(howConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(howConstruct('abcdef',['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(howConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(howConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e','ee','eee','eeee','eeeee','eeeeee']))