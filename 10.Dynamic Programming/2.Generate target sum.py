# Write a function canSum(targetSum,numbers) that takes in a targetSum and an array of numbers as an arguments.

# The function should return a boolean indicating whether or not it is possible to generate the targetSum using numbers from the array.

# You may use an element of the array as many times as needed.

# You may assume that all input numbers are non negatives.

# Naive approach using recurion

def canSum(targetSum,numbers):
    if targetSum == 0:
        return True
    if targetSum < 0 :
        return False
    
    for i in range(len(numbers)):
        if canSum(targetSum-numbers[i]) == True:
            return True
    return False

# TC : O(n^m)
# SC : O(m)

# Implementation using memoization /  Top-Down Approach 

def canSum(targetSum,numbers,memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for i in range(len(numbers)):
        if canSum(targetSum-numbers[i],numbers,memo) == True:
            memo[targetSum] = True
            return memo[targetSum]
    memo[targetSum] = False
    return memo[targetSum]

# TC : O(m*n)
# SC : O(m)