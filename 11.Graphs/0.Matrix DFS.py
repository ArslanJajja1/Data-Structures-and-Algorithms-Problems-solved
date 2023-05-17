# Problem

# Count the unique paths from the top left to the bottom right. A single path may only move along 0's and can't visit the same cell more than once.

# Count Paths ( Backtracking )

def dfs(grid,r,c,visit):
    ROWS,COLS = len(grid),len(grid[0])
    if (min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == 1):
        return 0
    if r == ROWS - 1 and c == COLS - 1:
        return 1
    visit.add((r,c))
    count = 0

    count += dfs(grid,r+1,c,visit)
    count += dfs(grid,r-1,c,visit)
    count += dfs(grid,r,c+1,visit)
    count += dfs(grid,r,c-1,visit)

    visit.remove((r,c))
    return count

grid =[ [0,0,0,0],
        [1,1,0,0],
        [0,0,0,1],
        [0,1,0,0] ]
print(dfs(grid,0,0,set()))

# TC : O(4^(m*n))
# SC : O(m*n)
