## Description ##
# Returns True if you can construct target string by concatenating elements of a list of strings 
# wordBank. 
# Returns false if you can't.
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

def canConstruct(target, wordBank, memo = {}):
    if memo is None: memo = {}
    
    if target in memo: return memo[target]
    elif target == '': return True
    
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            result = canConstruct(suffix, wordBank)
            if result == True: 
                memo[target] = True
                return True

    memo[target] = False
    return False

print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(canConstruct('enterapotentpot', ['a','p','ent','enter','ot','o','t']))
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e','ee','eee','eeee','eeeee','eeeeee']))