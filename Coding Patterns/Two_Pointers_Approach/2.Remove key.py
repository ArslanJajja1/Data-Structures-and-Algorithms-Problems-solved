# Problem 1: Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array.

# Example 1:

# Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
# Output: 4
# Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].
# Example 2:

# Input: [2, 11, 2, 2, 1], Key=2
# Output: 2
# Explanation: The first two elements after removing every 'Key' will be [11, 1].

def remove_key(nums,key):
    next = 0
    for i in range(len(nums)):
        if nums[i] != key:
            nums[next] = nums[i]
            next += 1
    return next
print(remove_key([3, 2, 3, 6, 3, 10, 9, 3], 3))
print(remove_key( [2, 11, 2, 2, 1], 2))

# Time and Space Complexity: The time complexity of the above algorithm will be O(N), where ‘N’ is the total number of elements in the given array.

# The algorithm runs in constant space O(1).