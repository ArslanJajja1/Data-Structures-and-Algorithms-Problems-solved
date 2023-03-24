# Problem Statement #
# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

# Example 1:

# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
# Example 2:

# Input: [2, 5, 9, 11], target=11
# Output: [0, 2]
# Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

def pair_with_target_sum(nums,target):
    i=0
    j=len(nums)-1
    while i <= j:
        if nums[i]+ nums[j] == target:
            return [i,j]
        elif nums[i]+nums[j] > target:
            j -= 1
        else:
            i += 1
    return []

print(pair_with_target_sum([1, 2, 3, 4, 6],6))
print(pair_with_target_sum([2, 5, 9, 11],11))

# Time Complexity #
# The time complexity of the above algorithm will be O(N), where ‘N’ is the total number of elements in the given array.

# Space Complexity #
# The algorithm runs in constant space O(1).