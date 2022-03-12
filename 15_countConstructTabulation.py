## Description ##
# Returns the number of ways that the 'target' can be constructed by concatenating elements of the 
# 'wordBank' array.
# Returns 0 if 'target' can't be constructed.
# 
# Reuse of elements in wordBank is allowed.

## Complexity ##
# let n = len(wordBank) and m = len(target)
#
# Time complexity of O(n*m^2). The extra m comes from checking the matching strings.
# Space complexity of O(m).

def countConstruct(target, wordBank):
    table = [0 for col in range(len(target) + 1)]
    table[0] = 1
    
    for i in range(len(target)):
        if table[i] > 0:
            for word in wordBank:
                if i+len(word) <= len(target) and target[i : i+len(word)] == word:
                    table[i+len(word)] += table[i]
    
    return table[len(target)]

print(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(countConstruct('enterapotentpot', ['a','p','ent','enter','ot','o','t']))
print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e','ee','eee','eeee','eeeee','eeeeee']))