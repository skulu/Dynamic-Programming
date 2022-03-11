# Return a boolean indicating if the targetsum can be generated by the numbers 
# in the array numbers. Assume all numbers in array are positive and you can 
# reuse the numbers as many times as you wish.

## 2D array solution ##
# def canSum(target, numbers):
#     n = len(numbers)
#     table = [[0 for col in range(n+1)] for row in range(n+1)]
    
#     table[0][1:n+1] = numbers[:]
#     for i in range(1,n+1):
#         table[i][0] = numbers[i-1]
    
#     for i in range(1,len(table)):
#         for j in range(1,len(table[0])):
#             table[i][j] = table[0][j] + table[0][i]
#             if table[i][j] == target: return True

#     return False

## 1D List solution ##
def canSum(target, numbers):
    table = [False for col in range(target+1)]
    table[0] = True # base case, then current amount + numbers[x] will also be True
    
    for i in range(target+1):
        for j in range(len(numbers)):
            if table[i] == True and (i+numbers[j]) < target+1:
                table[i+numbers[j]] = True
    
    return table[target]

print(canSum(7,[5,3,4]))
print(canSum(300,[7,14])) 