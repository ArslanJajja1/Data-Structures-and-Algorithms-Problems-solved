# Problem Statement #
# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.

# Example 1:

# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
# Example 2:

# Input: [2, 2, 2, 11]
# Output: 2
# Explanation: The first two elements after removing the duplicates will be [2, 11].

def remove_duplicates(arr):
    j = 0
    for i in range(1,len(arr)):
        if arr[i] != arr[j]:
            arr[i],arr[j+1] = arr[j+1],arr[i]
            j += 1
    return j+1


print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
print(remove_duplicates([2, 2, 2, 11]))

# Time Complexity : O(N)
# Space Complexity : O(1)