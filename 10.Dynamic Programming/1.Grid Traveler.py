# Say that you are a traveler on a 2D grid. You begin in the top-left corner and your goal is to travel to the bottom-right corner. You may only move down or right.

# In how many ways, can you travel to the goal on a grid with dimension m*n > 

# Write a function gridTraveler(m,n) that calculate this.

# Naive approach using recursion.

def gridTraveler(m,n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    count = 0
    count += gridTraveler(m-1,n)
    count += gridTraveler(m,n-1)
    return count

# TC : O(2^m*n)
# SC : O(m*n)

# Implementation using memoization /  Top-Down Approach

def gridTraveler(m,n,memo={}):
    if (m,n) in memo:
        return memo[(m,n)]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    count = 0
    count += gridTraveler(m-1,n,memo)
    count += gridTraveler(m,n-1,memo)
    memo[(m,n)] = count
    return memo[(m,n)]

# TC : O(m*n)
# SC : O(m*n)