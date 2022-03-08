# Return an array containing the shortest combination of numbers that will add up to the targetSum.
# 
# let n = len(numbers) and m = targetsum
# 
# Before memoization:
# O(n^m) in time
# O(m) in space
# 
# After memoization:
# O(n*m^2) in time. Extra multiplication in m to account for longest possible combination when you 
# do a copy of the list in line 29. Copy will need to access each element of the list.
# O(m^2) in space as combination is m in length at worst.



def bestSum(targetSum, numbers, memo = None):
    if memo is None: memo = {}

    if targetSum in memo: return memo[targetSum]
    elif targetSum == 0: return []
    elif targetSum < 0: return None

    
    shortestCombination = None
    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers, memo)
        if remainderCombination is not None:
            combination = [num] + remainderCombination
            if (shortestCombination is None) or (len(combination) < len(shortestCombination)):
                shortestCombination = combination

    memo[targetSum] = shortestCombination
    return shortestCombination

print(bestSum(7,[5,3,4,7]))
print(bestSum(8,[2,3,5]))
print(bestSum(8,[1,4,5]))
print(bestSum(100,[1,2,5,25]))
