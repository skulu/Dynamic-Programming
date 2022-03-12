
def howSum(target, numbers):
    table = [None for col in range(target+1)]
    table[0] = []

    for i in range(target):
        if table[i] is not None:
            for num in numbers:
                sumWay = table[i] + [num]
                summation = sum(sumWay)
                if summation <= target and table[summation] is None:
                    table[summation] = sumWay
    
    return table[target]

print(howSum(7,[2,3]))
print(howSum(7,[5,3,4,7]))
print(howSum(7,[2,4]))
print(howSum(8,[2,3,5]))
print(howSum(300,[7,14]))