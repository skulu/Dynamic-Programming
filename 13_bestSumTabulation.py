# Return an array containing the shortest combination of numbers that will add up to the targetSum.

def bestSum(target, numbers):
    table = [None for col in range(target+1)]
    table[0] = []

    for i in range(target):
        if table[i] is not None:
            for j in range(len(numbers)):
                sumWay = table[i] + [numbers[j]]
                summation = sum(sumWay)
                if summation <= target and table[summation] is None: 
                    # The table elements will always be filled first by the least number of 
                    # elements possible as you count up from the first element of the 
                    # table. Hence, don't insert unless that element is None.
                    table[summation] = sumWay
    
    return table[target]

print(bestSum(7,[2,3]))
print(bestSum(7,[5,3,4,7]))
print(bestSum(7,[2,4]))
print(bestSum(8,[2,3,5]))
print(bestSum(300,[7,14]))