
def howSum(target, numbers):
    table = [None for col in range(target+1)]
    
    for i in range(target):
        for j in range(len(numbers)):
            if (table[i] is None) and (numbers[j]) <= target:
                table[numbers[j]] = [numbers[j]]
            elif (table[i] is not None):
                sumWay = table[i] + [numbers[j]]
                summation = sum(sumWay)
                if summation <= target and table[summation] is None:
                    table[summation] = sumWay
    
    return table[target]

print(howSum(7,[2,3]))
print(howSum(7,[5,3,4,7]))
print(howSum(7,[2,4]))
print(howSum(8,[2,3,5]))
print(howSum(300,[7,14]))

#%%
# target = 7
# table = [1 for col in range(target+1)]

# sum(table)

# %%
