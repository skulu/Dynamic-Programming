# Function returns an array containing any combinantion of elements that add up 
# to exactly the targetSum. If there is no such combination, return Null. If 
# multiple combinations are possible, returning any one of them will suffice.

# let n = len(numbers) and m = targetsum
# O(n^m * m) in time, the extra m is for the copying of the list in line 20, 
# and O(m) in space before memoisation
# O(n*m^2) in time where the extra m is due to copying of the list in line 20.
# O(m^2) in space as your memo object now stores at most m items and each item 
# is at most m length to sum up to targetSum

def howSum(targetSum, numbers, memo = None):
    if memo is None: memo = {} # don't use mutables in function definition!!
    if targetSum == 0: return []
    elif targetSum < 0: return None
    elif targetSum in memo: return memo[targetSum]
    
    for num in numbers:
        remainder = targetSum - num
        result =  howSum(remainder, numbers, memo)
        if result is not None:
            memo[targetSum] = [num] + result
            return memo[targetSum]
    
    memo[targetSum] = None
    return None

print(howSum(7,[2,3]))
print(howSum(7,[5,3,4,7]))
print(howSum(7,[2,4]))
print(howSum(8,[2,3,5]))
print(howSum(300,[7,14]))
