# Given a grid of n rows by m columns, how many ways can a person move from the 
# top left to the bottom right if he can only move down or to the right?

# O(n*m) in time and space.

def gridTraveller(n,m):
    grid = [[0 for col in range(m+1)] for row in range(n+1)]
    grid[1][1] = 1

    for i in range(1,len(grid)):
        for j in range(1,len(grid[0])):
            grid[i][j] += grid[i-1][j] + grid[i][j-1]

    return grid[n][m]

print(gridTraveller(1,1))
print(gridTraveller(2,3))
print(gridTraveller(3,2))
print(gridTraveller(3,3))
print(gridTraveller(18,18))