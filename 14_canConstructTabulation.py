## Description ##
# Returns True if you can construct target string by concatenating elements of a list of strings 
# wordBank. 
# Returns false if you can't.
# 
# Reuse of elements in wordBank is allowed.

def canConstruct(target, wordBank):
    table = [False for col in range(len(target)+1)]
    table[0] = True
    
    for i in range(len(target)):
        if table[i] == True:
            for word in wordBank:
                if (i+len(word)) <= len(target) and target[i:i+len(word)] == word:
                    table[i+len(word)] = True
    return table[len(target)]

print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(canConstruct('enterapotentpot', ['a','p','ent','enter','ot','o','t']))
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e','ee','eee','eeee','eeeee','eeeeee']))
