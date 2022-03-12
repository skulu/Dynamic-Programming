## Description ##
# Returns the different combinations of words that the 'target' can be constructed by concatenating 
# elements of the 'wordBank' array. Returns 2D array with each element representing 1 way of 
# construction.
# 
# Reuse of elements in wordBank is allowed.

## Complexity ##
# let n = len(wordBank) and m = len(target)
#
# We will need to find all possible combinations and store all possible combinations. Hence: 
# Time complexity of O(n^m).
# Space complexity of O(n^m)

def allConstruct(target, wordBank):
    table = [[] for i in range(len(target)+1)]
    table[0] = [[]]

    for i in range(len(target)):
        if len(table[i]) > 0:
            for word in wordBank:
                if i+len(word) <= len(target) and target[i:i+len(word)] == word:
                    for j in range(len(table[i])):
                        table[i+len(word)].append(table[i][j] + [word])

    return table[len(target)]

print(allConstruct('', ['purp', 'p', 'ur', 'le', 'purpl']))
print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(allConstruct('abcdef',['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(allConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(allConstruct('eeeeeeeeeeeeeeeef', ['e','ee','eee','eeee','eeeee','eeeeee']))