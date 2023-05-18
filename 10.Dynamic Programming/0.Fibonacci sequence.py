# Write a function that takes a number as an argument and returns the nth number of the fibonacci sequence. The 1st and 2nd number of the sequence is 1. To generate the next number of the sequence,we sum the previous two.

# Naive approach using recursion

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1)+fib(n-2)

# TC : O(2^n)
# SC : O(n)

# Implementation using memoization # Top Down Approach

def fib(n,memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1,memo) + fib(n-2,memo)
    return memo[n]

# TC : O(n)
# SC : O(n)