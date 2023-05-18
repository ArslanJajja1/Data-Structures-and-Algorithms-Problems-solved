# Write a function howSum(targetSum,numbers) that takes in a targetSum and an array of numbers as arguments.

# The function should return an array containing any combination of elements that add up to exactly the targetSum. If there is no combination of that adds up to the targetSum, then return null.

# If there are multiple combinations possible, you may return any single one.


# Naive approach using recursion

# targetSum = 7 , numbers = [5,3,4,7]
def howSum(targetSum,numbers,ds):
    if targetSum == 0:
        return ds
    if targetSum < 0 :
        return None
    for i in range(len(numbers)):
        ds.append(numbers[i])
        if howSum(targetSum-numbers[i],numbers,ds) != None:
            return ds
        ds.pop()
    return None
    
print(howSum(7,[5,3,4,7],[]))