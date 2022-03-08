

def bestSum(targetSum, numbers):

    if targetSum == 0: return []
    elif targetSum < 0: return None
    
    shortestCombination = []
    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers)
        if remainderCombination is not None:
            combination = [num] + remainderCombination
            if (len(combination) < len(shortestCombination)) or len(shortestCombination) == 0:
                shortestCombination = combination

    if len(shortestCombination) > 0:
        return shortestCombination
    else:
        return None

# print(bestSum(4,[2,2]))
print(bestSum(7,[5,3,4,7]))
print(bestSum(8,[2,3,5]))
print(bestSum(8,[1,4,5]))
# print(bestSum(100,[1,2,5,25])

#%%
# a = [[2],[3]]

# for i in range(1,1):
#     a[i].append(i)

# print(a)

# %%
