# Return an array containing the shortest combination of numbers that will add up to the targetSum.

def bestSum(target, numbers):
    table = [None for col in range(target+1)]
    table[0] = []

    for i in range(target):
        if table[i] is not None:
            for num in numbers:
                sumWay = table[i] + [num]
                summation = sum(sumWay)
                if (summation <= target) and (table[summation] is None or len(table[summation]) > len(sumWay)): 
                    table[summation] = sumWay
    
    return table[target]

print(bestSum(7,[5,3,4,7]))
print(bestSum(8,[2,3,5]))
print(bestSum(8,[1,4,5]))
print(bestSum(100,[1,2,5,25]))